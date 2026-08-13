# Machine Learning — Road Accident Risk

## Objective
Build a baseline model that classifies Indian states/UTs into **Low, Medium, or High accident-risk** groups using the available government road-accident and Census population extracts.

## Pipeline
1. Load road accident data.
2. Load Census population data.
3. Join datasets using `state_ut`.
4. Engineer accidents, fatalities and injuries per 100,000 population.
5. Create relative risk classes using distribution-based terciles.
6. Train a Random Forest classifier.
7. Evaluate with accuracy and classification report.

## Run
From the repository root:

```bash
python src/ml/accident_risk_model.py
```

## Important interpretation
This is a **baseline analytical model**, not a production forecasting system. The current government extracts are cross-sectional/state-level and therefore do not support a reliable future-year prediction claim by themselves. A stronger forecasting model should be trained after adding multiple years of consistent state-level observations and time-based validation.
