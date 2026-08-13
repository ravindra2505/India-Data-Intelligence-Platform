from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_road_data_exists():
    p = ROOT / "data/raw/road_accidents/road_accidents_2024.csv"
    assert p.exists()
    df = pd.read_csv(p)
    assert len(df) > 1
    assert "road_accidents" in df.columns