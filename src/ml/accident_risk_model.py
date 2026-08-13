"""Road accident risk prediction model.

This module creates a reproducible baseline model from the available state-level
road accident and population extracts. It predicts accident-risk class using
accidents per 100,000 population and related state-level indicators.
"""

from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[2]
ROAD_PATH = ROOT / "data/raw/road_accidents/road_accidents_2024.csv"
POP_PATH = ROOT / "data/raw/population/census_2011_state_population.csv"


def load_features() -> pd.DataFrame:
    road = pd.read_csv(ROAD_PATH)
    population = pd.read_csv(POP_PATH)

    road = road[road["state_ut"].ne("All India")].copy()
    population = population[population["state_ut"].ne("All India")].copy()

    df = road.merge(population, on="state_ut", how="inner")
    df["accidents_per_100k"] = (
        df["road_accidents"] / df["population"] * 100_000
    )
    df["fatalities_per_100k"] = (
        df["persons_killed"] / df["population"] * 100_000
    )
    df["injuries_per_100k"] = (
        df["persons_injured"] / df["population"] * 100_000
    )

    # Relative risk classes: Low / Medium / High based on the distribution.
    df["risk_class"] = pd.qcut(
        df["accidents_per_100k"], q=3,
        labels=["Low", "Medium", "High"], duplicates="drop"
    )
    return df.dropna()


def train_model(df: pd.DataFrame):
    features = [
        "population",
        "road_accidents",
        "persons_killed",
        "persons_injured",
        "accidents_per_100k",
        "fatalities_per_100k",
        "injuries_per_100k",
    ]
    X = df[features]
    y = df["risk_class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200, random_state=42, class_weight="balanced"
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions, zero_division=0))
    return model


if __name__ == "__main__":
    data = load_features()
    model = train_model(data)
    print("Model trained successfully.")
