"""
End-to-end AI data pipeline:
- Cleans raw text data
- Validates labels
- Applies QA rules
- Produces cleaned data and QA report
"""

import pandas as pd
from pathlib import Path
from clean_text import clean_text

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "practice_dataset.csv"
CLEAN_DATA = BASE_DIR / "data" / "cleaned_dataset.csv"
QA_REPORT = BASE_DIR / "data" / "qa_report.txt"

ALLOWED_LABELS = {"neutral", "positive", "unsafe"}

def run_quality_checks(df: pd.DataFrame) -> dict:
    report = {}

    report["total_records"] = len(df)
    report["short_texts"] = (df["clean_text"].str.len() < 10).sum()
    report["duplicate_texts"] = df.duplicated(subset="clean_text").sum()
    report["invalid_labels"] = (~df["label"].isin(ALLOWED_LABELS)).sum()

    return report
def main():
    # Load raw data
    df = pd.read_csv(RAW_DATA)

    # Clean text
    df = clean_text(df)

    # Save cleaned data
    df.to_csv(CLEAN_DATA, index=False)

    # Run QA checks
    qa_results = run_quality_checks(df)

    # Write QA report
    with open(QA_REPORT, "w", encoding="utf-8") as f:
        for key, value in qa_results.items():
            f.write(f"{key}: {value}\n")

    print("Pipeline completed successfully.")
    print("Cleaned data:", CLEAN_DATA)
    print("QA report:", QA_REPORT)

if __name__ == "__main__":
    main()
