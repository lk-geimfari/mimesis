"""Script to run train ML model."""

from kfp.dsl import InputPath, OutputPath, component


@component(
    base_image="python:3.10",
    packages_to_install=[
        "google-cloud-aiplatform",
        "google-cloud-secret-manager",
        "gretel-client[gcp,tuner]",
        "git+https://github.com/gretelai/gretel-mlops",
        "imblearn",
        "optuna",
        "pandas",
        "scikit-learn",
        "xgboost",
    ],
)
def train_component(
    config: str,
    input_dir: InputPath(),
    gretel_dir: InputPath(),
    output_dir: OutputPath(),
):
    import json
    import logging
    import os

    import optuna
    import pandas as pd
    import xgboost as xgb

    from gretel_mlops.gcp.vertexai.utils import objective_func

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # parse config file
    config = json.loads(config)

    # Extract configuration details
    target_column = config["dataset"]["target_column"]
    ml_task = config["ML"]["ml_task"]
    ml_eval_metric = config["ML"]["ml_eval_metric"]
    objective = config["ML"]["objective"]
    objective_type = config["ML"]["objective_type"]

    # Reading training data
    logger.info("Reading train data.")
    X_train = pd.read_csv(f"{gretel_dir}/train.csv")
    y_train = X_train.pop(target_column)

    # Reading validation data
    logger.info("Reading validation data.")
    X_val = pd.read_csv(f"{input_dir}/validation.csv")
    y_val = X_val.pop(target_column)
    # Ensure the columns match between training and validation data
    X_val.columns = X_train.columns

    # Optuna study for hyperparameter optimization
    study = optuna.create_study(direction=objective_type.lower())
    study.optimize(
        lambda trial: objective_func(
            trial,
            X_train,
            y_train,
            X_val,
            y_val,
            ml_task,
            objective,
            ml_eval_metric,
        ),
        n_trials=6,
        n_jobs=2,
    )

    # Retrain the model with the best hyperparameters
    best_params = study.best_trial.params
    if ml_task == "regression":
        final_model = xgb.XGBRegressor(**best_params)
        final_model.fit(X_train, y_train)
    else:
        final_model = xgb.XGBClassifier(**best_params)
        final_model.fit(X_train, y_train)

    # Save the model and best hyperparameters to files
    logger.info("Saving the final model and best parameters.")
    final_model.save_model(f"{output_dir}/model.bst")
    with open(f"{output_dir}/best_params.json", "w") as f:
        json.dump(best_params, f)
