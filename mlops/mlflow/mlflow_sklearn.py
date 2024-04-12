# ML FLOW CONFIG FILE FOR SKLEARN

from pprint import pprint
import numpy as np

import mlflow
from mlflow import MlflowClient


def fetch_logged_data(run_id):
    client = MlflowClient()
    data = client.get_run(run_id).data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts


# enable autologging
mlflow.sklearn.autolog()



# train a model
model = LinearRegression()
with mlflow.start_run() as run:
    model.fit(X, y)

# fetch logged data
params, metrics, tags, artifacts = fetch_logged_data(run.info.run_id)

pprint(params)
# {'copy_X': 'True',
#  'fit_intercept': 'True',
#  'n_jobs': 'None',
#  'normalize': 'False'}

pprint(metrics)
# {'training_score': 1.0,
#  'training_mean_absolute_error': 2.220446049250313e-16,
#  'training_mean_squared_error': 1.9721522630525295e-31,
#  'training_r2_score': 1.0,
#  'training_root_mean_squared_error': 4.440892098500626e-16}

pprint(tags)
# {'estimator_class': 'sklearn.linear_model._base.LinearRegression',
#  'estimator_name': 'LinearRegression'}

pprint(artifacts)
# ['model/MLmodel', 'model/conda.yaml', 'model/model.pkl']