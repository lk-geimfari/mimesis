import numpy as np
import optuna
import pandas as pd
import xgboost as xgb
from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
from google.cloud import secretmanager
from gretel_client.projects.models import Model
from gretel_client.tuner import BaseTunerMetric, MetricDirection
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import (average_precision_score, confusion_matrix,
                             mean_absolute_error, mean_squared_error,
                             precision_recall_curve, r2_score, roc_auc_score)


def get_secret(secret_id, project_number):

    """
    Retrieves a secret value from Google Cloud Secret Manager.

    This function initializes a Secret Manager client using the given project number,
    constructs the resource ID of the secret, and then accesses the latest version
    of the specified secret.

    Args:
        secret_id (str): The ID of the secret to retrieve.
        project_number (str): The project number where the secret is stored.

    Returns:
        str: The secret value as a string if the retrieval is successful; None otherwise.
    """
 
    # Initialize the client
    client = secretmanager.SecretManagerServiceClient()
    secret_version = (
        f"projects/{project_number}/secrets/{secret_id}/versions/latest"
    )

    try:
        response = client.access_secret_version(
            request={"name": secret_version}
        )
        gretel_api_key = response.payload.data.decode("UTF-8")
        return gretel_api_key
    except PermissionDenied as e:
        print(f"Permission denied: {e.message}")
        return None
    except GoogleAPICallError as e:
        print(f"An error occurred accessing the secret: {e}")
        return None


def naive_upsample(df, target_column, target_balance=1.0):
    """
    Upsamples a DataFrame to balance classes in the target column.

    Args:
        df (pd.DataFrame): The DataFrame to upsample.
        target_column (str): The target column for class balancing.
        target_balance (float): The desired balance ratio.

    Returns:
        pd.DataFrame: The upsampled DataFrame.
    """
    # Initialize the over-sampler
    over_sampler = RandomOverSampler(sampling_strategy=target_balance)
    y = df.pop(target_column)
    df_resampled, y_resampled = over_sampler.fit_resample(df, y)
    df_resampled[target_column] = y_resampled

    return df_resampled


def compute_optimal_f1(y_test, predictions):
    """
    Computes the optimal F1 score for binary classification predictions.

    Args:
        y_test (np.ndarray): True binary labels.
        predictions (np.ndarray): Predicted probabilities.

    Returns:
        tuple: Best F1 score, optimal precision, optimal recall, and
            confusion matrix.
    """
    # Compute precision-recall curve
    precision, recall, thresholds = precision_recall_curve(y_test, predictions)

    # Remove zero precision and recall values
    selection = ~((precision == 0) & (recall == 0))
    precision = precision[selection]
    recall = recall[selection]
    thresholds = thresholds[selection[:-1]]

    # Calculate F1 scores and find the threshold that maximizes it
    f1_scores = 2 * (precision * recall) / (precision + recall)
    best_threshold = thresholds[np.argmax(f1_scores)]
    best_f1_score = np.max(f1_scores)

    # Calculate precision and recall at the optimal threshold
    optimal_precision = precision[np.argmax(f1_scores)]
    optimal_recall = recall[np.argmax(f1_scores)]

    # Compute confusion matrix at the optimal threshold
    predictions_binary = (predictions >= best_threshold).astype(int)
    conf_matrix = confusion_matrix(y_test, predictions_binary)

    return best_f1_score, optimal_precision, optimal_recall, conf_matrix


def generate_classification_report(y_test, predictions):
    """
    Generates a report containing various classification metrics.

    Args:
        y_test (np.ndarray): True binary labels.
        predictions (np.ndarray): Predicted probabilities.

    Returns:
        dict: A dictionary containing classification metrics.
    """
    # Compute classification metrics
    f1, precision, recall, conf_matrix = compute_optimal_f1(
        y_test, predictions
    )
    roc_auc = roc_auc_score(y_test, predictions)
    pr_auc = average_precision_score(y_test, predictions)

    # Assemble the metrics into a report dictionary
    report_dict = {
        "metrics": {
            "auc": {"value": roc_auc},
            "aucpr": {"value": pr_auc},
            "precision": {"value": precision},
            "recall": {"value": recall},
            "f1": {"value": f1},
            "confusion_matrix": {"value": conf_matrix.tolist()},
        },
    }

    return report_dict


def generate_regression_report(y_test, predictions):
    """
    Generates a report containing various regression metrics.

    Args:
        y_test (np.ndarray): True values.
        predictions (np.ndarray): Predicted values.

    Returns:
        dict: A dictionary containing regression metrics.
    """
    # Calculate regression metrics
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Calculate standard deviations for each metric
    mse_std = np.std((y_test - predictions) ** 2)
    rmse_std = np.std(np.abs(y_test - predictions))
    mae_std = np.std(np.abs(y_test - predictions))
    r2_std = np.std(
        1 - ((y_test - predictions) ** 2) / ((y_test - np.mean(y_test)) ** 2)
    )

    # Assemble the metrics into a report dictionary
    report_dict = {
        "metrics": {
            "mse": {"value": mse, "std": mse_std},
            "mae": {"value": mae, "std": mae_std},
            "R2": {"value": r2, "std": r2_std},
            "rmse": {"value": rmse, "std": rmse_std},
        },
    }

    return report_dict


def objective_func(
    trial, X_train, y_train, X_val, y_val, task, objective, metric
):
    """
    Objective function for Optuna hyperparameter optimization.

    Args:
        trial (optuna.trial.Trial): A single trial from Optuna.
        X_train (pd.DataFrame): Training feature data.
        y_train (pd.Series): Training target data.
        X_val (pd.DataFrame): Validation feature data.
        y_val (pd.Series): Validation target data.
        task (str): Type of machine learning task ('regression' or
            'classification').
        objective (str): Objective function for the XGBoost model.
        metric (str): Metric to optimize.

    Returns:
        float: The computed metric value for the trial.
    """
    # Define hyperparameter search space for the XGBoost model
    param = {
        "silent": 0,
        "verbosity": 0,
        "objective": objective,
        "eta": trial.suggest_float("eta", 0, 1),
        "min_child_weight": trial.suggest_float("min_child_weight", 1, 10),
        "alpha": trial.suggest_float("alpha", 0, 2),
        "max_depth": trial.suggest_int("max_depth", 1, 10),
        "num_round": trial.suggest_int("num_round", 100, 500),
        "rate_drop": 0.3,
        "tweedie_variance_power": 1.4,
    }

    # Train and evaluate the model based on the task
    if task == "regression":
        model = xgb.XGBRegressor(**param)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        score = generate_regression_report(y_val, y_pred)["metrics"]
    else:
        model = xgb.XGBClassifier(**param)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        score = generate_classification_report(y_val, y_pred)["metrics"]

    return score[metric]["value"]


class MLMetric(BaseTunerMetric):
    """
    Custom metric for ML model evaluation

    Args:
        df_test (pd.DataFrame): The test dataset.
        preprocess (object): Preprocessing steps applied to the data.
        target_column (str): Name of the target column.
        metric (str, optional): Name of the metric to optimize.
        task (str, optional): Type of machine learning task.
        objective (str, optional): Objective function for the XGBoost model.
        objective_type (str, optional): Direction of optimization ('Maximize'
            or 'Minimize').
    """

    def __init__(
        self,
        df_test,
        preprocess,
        target_column,
        metric="f1",
        task="classification",
        objective="binary:logistic",
        objective_type="Maximize",
    ):
        self.df_test = df_test
        self.metric = metric
        self.task = task
        self.preprocess = preprocess
        self.target_column = target_column
        self.objective = objective
        self.direction = MetricDirection[objective_type.upper()]

    def __call__(self, model: Model):
        """
        Evaluates the model using Optuna.

        Args:
            model (Model): The Gretel synthetic model to be evaluated.

        Returns:
            float: The best value of the specified metric.
        """
        # Load and preprocess the training data from the model's artifact
        X_train = pd.read_csv(
            model.get_artifact_link("data_preview"), compression="gzip"
        )
        y_train = X_train.pop(self.target_column)
        X_train = pd.DataFrame(self.preprocess.transform(X_train))

        # Align the columns of the test set to match those of the training set
        X_val = self.df_test.copy()
        y_val = X_val.pop(self.target_column)
        X_val.columns = X_train.columns

        # Create and run an Optuna study for hyperparameter optimization
        study = optuna.create_study(direction=self.direction.value)
        study.optimize(
            lambda trial: objective_func(
                trial,
                X_train,
                y_train,
                X_val,
                y_val,
                self.task,
                self.objective,
                self.metric,
            ),
            n_trials=6,
            n_jobs=2,
        )

        return study.best_value
