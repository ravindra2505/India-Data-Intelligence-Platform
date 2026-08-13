# 🇮🇳 India Data Intelligence Platform

> **Integrated Government Data Analytics & Decision Support System**

A clean, end-to-end data analytics project that combines published Indian government datasets across **road safety, weather, air quality, population, and vehicle mobility** into one reproducible analytical platform.

## 🎯 What problem does it solve?

Government information is published across different departments and formats. This project brings selected datasets together so analysts and decision-makers can answer questions such as:

- Which states report the highest road-accident burden?
- Where are fatalities and injuries most concentrated?
- How does accident burden compare with population size?
- What do rainfall and air-quality indicators look like across the available coverage?
- How is EV registration changing over time?
- Which states fall into relative road-accident risk groups?

## 🧩 Architecture

```text
Government Sources
       ↓
   Raw CSV Data
       ↓
 ETL / Validation
       ↓
Processed Analytics Data
       ↓
 ┌──────────┬────────────┬─────────────┐
 │   SQL    │ Streamlit  │  Power BI   │
 └──────────┴────────────┴─────────────┘
       ↓
 ML Risk Classification
       ↓
 Decision-Support Insights
```

## 📊 Data domains

| Domain | Source | Coverage |
|---|---|---|
| Road Safety | Ministry of Road Transport & Highways | 2024 |
| Weather | India Meteorological Department | 2020–2024 |
| Air Quality | MoEFCC / CPCB | 2023–24, selected West Bengal cities |
| Population | Census of India | 2011 |
| Vehicles | Vahan / Ministry of Heavy Industries | Through FY 2024–25 |

**Data note:** The datasets are government-published/report-based extracts. Coverage periods differ because each department publishes its own reporting series. Always display the source period and unit before making comparisons.

## 🛠️ Technology stack

- **Python** — core analytics
- **Pandas** — data processing
- **Scikit-learn** — machine learning
- **SQL** — analytical queries
- **Streamlit** — interactive application
- **Power BI** — business intelligence dashboards
- **Git & GitHub** — version control

## 📁 Project structure

```text
India-Data-Intelligence-Platform/
│
├── data/
│   ├── raw/
│   │   ├── road_accidents/
│   │   ├── weather/
│   │   ├── air_quality/
│   │   ├── population/
│   │   └── vehicles/
│   ├── processed/
│   └── external/
│
├── notebooks/
├── src/
│   ├── ml/
│   │   ├── accident_risk_model.py
│   │   └── README.md
│   ├── etl.py
│   └── database/
│
├── streamlit_app/
│   └── app.py
│
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
│
├── powerbi/
│   └── README.md
│
├── tests/
├── reports/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run locally

```bash
git clone https://github.com/ravindra2505/India-Data-Intelligence-Platform.git
cd India-Data-Intelligence-Platform

python -m venv venv

# Windows PowerShell
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

If PowerShell blocks activation, run the Streamlit command from a terminal where the environment is available, or use Command Prompt with `venv\\Scripts\\activate.bat`.

## 🤖 Machine Learning

The current ML component is a **baseline relative-risk classifier**. It engineers accidents, fatalities and injuries per 100,000 population and classifies states/UTs into Low, Medium and High relative-risk groups using a Random Forest model.

This should not be described as future accident forecasting: the current extracts do not provide enough consistent multi-year state-level observations for a defensible time-series forecast.

## 📈 SQL analytics

The SQL layer contains reusable queries for:

- State accident ranking
- Fatality ranking
- Fatality rate
- Accidents per 100,000 population
- Population ranking
- EV growth
- Rainfall deviation
- PM10 summaries

## 📊 Streamlit dashboard

The application contains:

1. **Executive Overview** — key KPIs and data coverage
2. **Road Safety** — state-level accident analysis
3. **Environment** — air-quality and weather data
4. **Demographics & Mobility** — population and EV trends
5. **Data Explorer** — direct dataset exploration

## 🔍 Data quality principles

- Preserve source values before transformation.
- Keep dataset coverage periods visible.
- Avoid mixing incompatible units or years without explanation.
- Validate joins before producing cross-domain KPIs.
- Separate exploratory analysis from decision-support claims.

## 📚 Official sources

- Ministry of Road Transport & Highways — https://morth.gov.in/
- Open Government Data Platform India — https://data.gov.in/
- Census of India — https://censusindia.gov.in/
- India Meteorological Department — https://mausam.imd.gov.in/
- Central Pollution Control Board — https://cpcb.nic.in/
- Ministry of Heavy Industries — https://heavyindustries.gov.in/

## 👤 Project

**India Data Intelligence Platform**

Built as an end-to-end portfolio project demonstrating data ingestion, validation, analytics, SQL, visualization, machine learning, documentation, and reproducible software practices.

> **Disclaimer:** This project is for analytical and educational purposes. Government datasets have different coverage periods, definitions, and reporting methodologies; cross-domain comparisons should be interpreted accordingly.
