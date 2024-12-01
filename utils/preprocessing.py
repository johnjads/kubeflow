"""
Author: Johnson
Description: This utility script preprocesses text data for ingestion into AutoML NLP by formatting a CSV file with 'text' and 'label' columns.
"""

import csv

def preprocess_csv(input_csv, output_csv):
    """
    Prepares a CSV file for AutoML NLP ingestion.

    Args:
        input_csv (str): Path to the raw input CSV file.
        output_csv (str): Path to save the processed CSV file.
    """
    with open(input_csv, "r") as infile, open(output_csv, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)

        # AutoML requires specific header: text, label
        writer.writerow(["text", "label"])
        for row in reader:
            writer.writerow([row["text"], row["label"]])
    print(f"Processed data saved to {output_csv}")

if __name__ == "__main__":
    # Argument parser for CLI usage
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess CSV for AutoML NLP")
    parser.add_argument("--input_csv", required=True, help="Path to input CSV file")
    parser.add_argument("--output_csv", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    preprocess_csv(args.input_csv, args.output_csv)
