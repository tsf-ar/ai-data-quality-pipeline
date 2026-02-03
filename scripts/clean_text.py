import pandas as pd
from pathlib import Path

# Get project root (ai-data-python)
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "practice_dataset.csv"
OUTPUT_PATH = BASE_DIR / "data" / "cleaned_dataset.csv"


def clean_text(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["clean_text"] = (
        df["text"]
        .str.replace(r"[!؟،,.]+", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    return df


def main():
    df = pd.read_csv(INPUT_PATH)
    df = clean_text(df)
    df.to_csv(OUTPUT_PATH, index=False)
    print("Cleaned data saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
