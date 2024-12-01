"""
Author: Johnson
Description: This script creates a dataset in Google AutoML for NLP tasks. The dataset is configured for multi-class classification and stored in the specified GCP project and region.
"""

from google.cloud import automl_v1beta1 as automl
import argparse

def create_dataset(project_id, region, dataset_name):
    """
    Creates a dataset in AutoML for text classification.

    Args:
        project_id (str): The GCP Project ID.
        region (str): The GCP region where AutoML is hosted.
        dataset_name (str): Display name of the dataset.

    Returns:
        str: Name of the created dataset.
    """
    client = automl.AutoMlClient()
    location_path = f"projects/{project_id}/locations/{region}"

    # Define dataset metadata for NLP
    dataset = {
        "display_name": dataset_name,
        "text_classification_dataset_metadata": {"classification_type": "MULTICLASS"}
    }

    # Create dataset
    response = client.create_dataset(parent=location_path, dataset=dataset)
    dataset_name = response.result().name
    print(f"Dataset created: {dataset_name}")
    return dataset_name

if __name__ == "__main__":
    # Argument parser for CLI usage
    parser = argparse.ArgumentParser(description="Create a dataset for AutoML NLP")
    parser.add_argument("--project_id", required=True, help="GCP Project ID")
    parser.add_argument("--region", required=True, help="GCP Region")
    parser.add_argument("--dataset_name", required=True, help="Dataset display name")
    args = parser.parse_args()

    create_dataset(args.project_id, args.region, args.dataset_name)
