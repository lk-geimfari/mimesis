import json

import google.cloud.aiplatform as aip
import pandas as pd
from kfp import dsl

from .components import (evaluate_component, gretel_component,
                         preprocess_component, register_component,
                         train_component)


def create_pipeline(
    pipeline_name,
    pipeline_root,
    model_display_name,
    model_image_uri,
    project_id,
    region,
    gretel_secret,
    project_number,
    config,
):
    """
    Create a pipeline for running a machine learning workflow.

    Args:
    pipeline_name (str): Name of the pipeline.
    pipeline_root (str): Path to the root directory of the pipeline.
    model_display_name (str): Display name of the model.
    model_image_uri (str): URI of the container image used for the model.
    project_id (str): Google Cloud project ID.
    region (str): Google Cloud region.
    gretel_secret (str): Secret key for Gretel.
    project_number (str): Google Cloud project number.
    config (dict): Configuration parameters for the pipeline.

    Returns:
    dsl.pipeline: A Kubeflow pipeline function.
    """

    @dsl.pipeline(
        name=pipeline_name,
        pipeline_root=pipeline_root,
    )
    def pipeline():
        # Preprocessing operation
        preprocess_op = preprocess_component(config=config)

        # Gretel synthetic data generation operation
        gretel_op = gretel_component(
            config=config,
            input_dir=preprocess_op.output,
            gretel_secret=gretel_secret,
            project_number=project_number,
        )

        # Model training operation
        train_op = train_component(
            config=config,
            input_dir=preprocess_op.output,
            gretel_dir=gretel_op.output,
        )

        # Model evaluation operation
        eval_op = evaluate_component(
            config=config,
            input_dir=preprocess_op.output,
            model_dir=train_op.output,
        )

        # Model registration operation
        register_component(
            config=config,
            model_display_name=model_display_name,
            model_image_uri=model_image_uri,
            project=project_id,
            location=region,
            eval_dir=eval_op.output,
            model_dir=train_op.output,
        )

    return pipeline


def get_pipeline_job_result(job_name: str, project: str, location: str):
    """
    Retrieve and display the result of a pipeline job.

    Args:
    job_name (str): Name of the pipeline job.
    project (str): Google Cloud project ID.
    location (str): Google Cloud region.

    Returns:
    str: JSON string of the evaluation report.
    """
    aip.init(project=project, location=location)

    # Get the job using the job name
    pipeline_job = aip.PipelineJob.get(resource_name=job_name)

    # Ensure the job is completed
    if str(pipeline_job.state) != "PipelineState.PIPELINE_STATE_SUCCEEDED":
        print(
            f"The job state is {pipeline_job.state}, "
            "please wait until it's completed."
        )
        return None

    # Get evaluation task details
    tasks_dict = {task.task_name: task for task in pipeline_job.task_details}
    eval_task = tasks_dict.get("evaluate-component")

    # Retrieve and parse the evaluation report
    evaluation_path = (
        f"{dict(eval_task.outputs)['output_dir'].artifacts[0].uri}"
        "/evaluation.json"
    )
    evaluation_report = json.loads(pd.read_json(evaluation_path).to_json())

    return json.dumps(evaluation_report, indent=4)
