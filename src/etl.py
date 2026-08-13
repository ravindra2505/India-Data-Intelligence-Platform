from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(ROOT / path)

if __name__ == "__main__":
    df = load_dataset("data/raw/road_accidents/road_accidents_2024.csv")
    print(df.head())