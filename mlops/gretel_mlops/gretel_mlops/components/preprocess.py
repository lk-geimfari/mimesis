"""Script to preprocess source data."""

from kfp.dsl import OutputPath, component


@component(
    base_image="python:3.10",
    packages_to_install=[
        "scikit-learn",
        "gcsfs",
        "pandas",
        "google-cloud-aiplatform",
    ],
)
def preprocess_component(config: str, output_dir: OutputPath()):
    import json
    import logging
    import os

    import joblib
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # parse config file
    config = json.loads(config)

    # Extract configuration details
    train_path = config["dataset"]["train_path"]
    test_path = config["dataset"]["test_path"]
    validation_path = config["dataset"]["validation_path"]
    target_column = config["dataset"]["target_column"]
    drop_columns = config["dataset"]["drop_columns"]
    ml_task = config["ML"]["ml_task"]

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read and preprocess training data
    logger.info("Reading in dataset.")
    df = pd.read_csv(train_path)
    # Define feature columns
    feature_columns = [col for col in df.columns if col != target_column]
    # Drop specified columns if any
    if drop_columns:
        df.drop(drop_columns, axis=1, inplace=True)
        used_cols = [col for col in feature_columns if col not in drop_columns]
    else:
        used_cols = feature_columns

    # Setup transformers for numeric and categorical features
    logger.debug("Defining transformers.")
    categorical_features = (
        df[used_cols]
        .select_dtypes(include=["object", "category"])
        .columns.tolist()
    )
    numeric_features = [
        col for col in used_cols if col not in categorical_features
    ]
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="constant", fill_value="missing"),
            ),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocess = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ],
        sparse_threshold=0,
    )

    # Convert target column for classification tasks
    logger.info("Convert target colum into integer categories.")
    if ml_task == "classification":
        df[target_column] = pd.Categorical(df[target_column])
        df[target_column] = df[target_column].cat.codes

    # Apply transforms to the data
    logger.info("Applying transforms.")
    X_train = df.sample(frac=1).reset_index(drop=True)
    y_train = X_train.pop(target_column)
    preprocess.fit(X_train)

    # Serialize and save the preprocessing object
    logger.info("Writing out preprocessing object")
    joblib.dump(preprocess, f"{output_dir}/preprocess.joblib")

    # Split data into train, validation, and test datasets
    logger.info(
        "Splitting %d rows of data into train, validation, test datasets.",
        len(X_train),
    )
    if test_path:
        logger.info("Processing test dataset.")
        # Read and preprocess test data
        df_test = pd.read_csv(test_path)
        X_test = df_test.sample(frac=1).reset_index(drop=True)
        y_test = X_test.pop(target_column)
    else:
        # Split the training data into training and test sets
        logger.info("Splitting train dataset into train and test subsets.")
        X_train, X_test, y_train, y_test = train_test_split(
            X_train,
            y_train,
            test_size=0.20,
            random_state=42,
            stratify=y_train if ml_task == "classification" else None,
        )

    # Check if a separate validation dataset path is provided
    if validation_path:
        logger.info("Processing validation dataset.")
        # Read and preprocess validation data
        df_valid = pd.read_csv(validation_path)
        X_valid = df_valid.sample(frac=1).reset_index(drop=True)
        y_valid = X_valid.pop(target_column)
    else:
        # Split the training data into training and validation sets
        logger.info(
            "Splitting train dataset into train and validation subsets."
        )
        X_train, X_valid, y_train, y_valid = train_test_split(
            X_train,
            y_train,
            test_size=0.25,
            random_state=42,
            stratify=y_train if ml_task == "classification" else None,
        )

    # Process and save the train dataset
    logger.info("Writing out train datasets")
    train_pre = pd.DataFrame(preprocess.transform(X_train))
    train = pd.concat([y_train.reset_index(drop=True), train_pre], axis=1)
    train.to_csv(f"{output_dir}/train.csv", header=True, index=False)

    # Process and save the validation dataset
    logger.info("Writing out validation dataset")
    validation_pre = pd.DataFrame(preprocess.transform(X_valid))
    validation = pd.concat(
        [y_valid.reset_index(drop=True), validation_pre], axis=1
    )
    validation.to_csv(f"{output_dir}/validation.csv", header=True, index=False)

    # Process and save the test dataset
    logger.info("Writing out test dataset")
    test_pre = pd.DataFrame(preprocess.transform(X_test))
    test = pd.concat([y_test.reset_index(drop=True), test_pre], axis=1)
    test.to_csv(f"{output_dir}/test.csv", header=True, index=False)

    # Save the original training data for further reference or use
    logger.info("Writing out original training data.")
    train_source = X_train
    train_source[target_column] = y_train
    train_source.to_csv(
        f"{output_dir}/train_source.csv", header=True, index=False
    )
