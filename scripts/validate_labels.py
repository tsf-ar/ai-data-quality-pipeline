import pandas as pd
from pathlib import Path

# Project root directory (ai-data-python)
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to cleaned dataset
DATA_PATH = BASE_DIR / "data" / "cleaned_dataset.csv"

ALLOWED_LABELS = {"neutral", "positive", "unsafe"}

def main():
    df = pd.read_csv(DATA_PATH)

    invalid_rows = df[~df["label"].isin(ALLOWED_LABELS)]

    if invalid_rows.empty:
        print("All labels are valid.")
    else:
        print("Invalid labels found:")
        print(invalid_rows)

if __name__ == "__main__":
    main()
