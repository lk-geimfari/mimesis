"""Evaluation script to assess ML model performance."""

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
def evaluate_component(
    config: str,
    input_dir: InputPath(),
    model_dir: InputPath(),
    output_dir: OutputPath(),
):
    import json
    import logging
    import os

    import pandas as pd
    import xgboost as xgb

    from gretel_mlops.gcp.vertexai.utils import (
        generate_classification_report, generate_regression_report)

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

    # Load the xgboost model
    logger.info("Loading xgboost model.")
    model = xgb.Booster()
    model.load_model(f"{model_dir}/model.bst")

    # Load the test data
    logger.info("Reading test data.")
    df = pd.read_csv(f"{input_dir}/test.csv")

    # Separate features and target variable from test data
    logger.info("Preparing test data.")
    y_test = df.pop(target_column)
    X_test = xgb.DMatrix(df.values)

    # Perform predictions using the xgboost model
    logger.info("Performing predictions against test data.")
    predictions = model.predict(X_test)

    # Calculate and generate the ML metrics based on the task
    logger.info("Calculating ML metrics.")
    if ml_task == "regression":
        report_dict = generate_regression_report(y_test, predictions)
    else:
        report_dict = generate_classification_report(y_test, predictions)
    logger.info(f"Creating Report: {report_dict}")

    # Write the evaluation report to a file
    logger.info("Writing out evaluation report")
    with open(f"{output_dir}/evaluation.json", "w") as f:
        f.write(json.dumps(report_dict))
