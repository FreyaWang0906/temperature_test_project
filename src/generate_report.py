import pandas as pd
from src.error_diagnosis import batch_diagnose
import os


def generate_report(input_csv, output_csv):

    df = pd.read_csv(input_csv)

    temps = df["Temperature"]. tolist()

    diagnosis_list = batch_diagnose(temps)
    df["diagnosis"] = diagnosis_list

    summary = df["diagnosis"]. value_counts()

    print("Diagnostic Statistics: ")
    print(summary. to_string())

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index= False)

    print(f"Report saved to {output_csv} ")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(base_dir, "..", "data", "temperature_log.csv")
    input_file = input_csv
    output_dir = os.path.join(base_dir, "..", "output")

    os.makedirs(output_dir,exist_ok=True)

    output_file = os.path.join(output_dir, "tempreture_report.csv")

    generate_report(input_file, output_file)
    print(f"Report generated at: {output_file}")






