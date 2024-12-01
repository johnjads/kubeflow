"""
Author: Johnson
Description: This script deploys a trained NLP model from Google AutoML to a managed endpoint for serving predictions.
"""

from google.cloud import automl_v1beta1 as automl
import argparse

def deploy_model(project_id, region, model_id):
    """
    Deploys a trained model to an AutoML endpoint.

    Args:
        project_id (str): The GCP Project ID.
        region (str): The GCP region where AutoML is hosted.
        model_id (str): ID of the trained model.

    Returns:
        str: Path of the deployed model.
    """
    client = automl.AutoMlClient()
    model_path = f"projects/{project_id}/locations/{region}/models/{model_id}"

    # Deploy model
    response = client.deploy_model(name=model_path)
    print("Model successfully deployed.")
    return model_path

if __name__ == "__main__":
    # Argument parser for CLI usage
    parser = argparse.ArgumentParser(description="Deploy an AutoML NLP Model")
    parser.add_argument("--project_id", required=True, help="GCP Project ID")
    parser.add_argument("--region", required=True, help="GCP Region")
    parser.add_argument("--model_id", required=True, help="Trained Model ID")
    args = parser.parse_args()

    deploy_model(args.project_id, args.region, args.model_id)
