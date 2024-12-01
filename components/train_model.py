"""
Author: Johnson
Description: This script trains an NLP model in Google AutoML using a specified dataset. It supports multi-class classification.
"""

from google.cloud import automl_v1beta1 as automl
import argparse

def train_model(project_id, region, dataset_id, model_name):
    """
    Trains a model in AutoML using a specified dataset.

    Args:
        project_id (str): The GCP Project ID.
        region (str): The GCP region where AutoML is hosted.
        dataset_id (str): ID of the dataset to be used for training.
        model_name (str): Display name of the model.

    Returns:
        str: Name of the trained model.
    """
    client = automl.AutoMlClient()
    location_path = f"projects/{project_id}/locations/{region}"

    # Define model metadata
    model = {
        "display_name": model_name,
        "dataset_id": dataset_id,
        "text_classification_model_metadata": {}
    }

    # Train model
    response = client.create_model(parent=location_path, model=model)
    print("Training initiated. This process may take several hours.")
    model_name = response.result().name
    print(f"Model training complete: {model_name}")
    return model_name

if __name__ == "__main__":
    # Argument parser for CLI usage
    parser = argparse.ArgumentParser(description="Train an AutoML NLP Model")
    parser.add_argument("--project_id", required=True, help="GCP Project ID")
    parser.add_argument("--region", required=True, help="GCP Region")
    parser.add_argument("--dataset_id", required=True, help="Dataset ID")
    parser.add_argument("--model_name", required=True, help="Model display name")
    args = parser.parse_args()

    train_model(args.project_id, args.region, args.dataset_id, args.model_name)
