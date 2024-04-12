"""Script to register ML model to model registry."""

from kfp.dsl import InputPath, component


@component(
    base_image="python:3.10",
    packages_to_install=["pandas", "google-cloud-aiplatform"],
)
def register_component(
    config: str,
    model_display_name: str,
    model_image_uri: str,
    project: str,
    location: str,
    eval_dir: InputPath(),
    model_dir: InputPath(),
):
    import json
    import logging

    import pandas as pd
    from google.cloud import aiplatform

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    # parse config file
    config = json.loads(config)

    # Extract configuration details
    ml_metric_threshold = config["ML"]["ml_metric_threshold"]
    ml_eval_metric = config["ML"]["ml_eval_metric"]
    objective_type = config["ML"]["objective_type"]

    # parse evaluation report
    evaluation_report = json.loads(
        pd.read_json(f"{eval_dir}/evaluation.json").to_json()
    )

    # Check if the evaluation metric exceeds the threshold
    if objective_type.lower() == "maximize":
        meets_condition = (
            evaluation_report["metrics"][ml_eval_metric]["value"]
            >= ml_metric_threshold
        )
    else:
        meets_condition = (
            evaluation_report["metrics"][ml_eval_metric]["value"]
            <= ml_metric_threshold
        )

    if meets_condition:
        logger.info(
            f"Evaluation metric {ml_eval_metric} exceeds "
            f"threshold {ml_metric_threshold}."
        )

        # Initialize AI Platform with the specified project and location
        aiplatform.init(project=project, location=location)

        # Register the model with AI Platform
        model_to_register = aiplatform.Model.upload(
            display_name=model_display_name,
            artifact_uri=model_dir,
            serving_container_image_uri=model_image_uri,
        )
        logger.info(
            f"Model {model_display_name} registered "
            f"with ID: {model_to_register.resource_name}"
        )

    else:
        logger.info(
            f"Evaluation metric {ml_eval_metric} does not exceed "
            f"threshold {ml_metric_threshold}"
        )
