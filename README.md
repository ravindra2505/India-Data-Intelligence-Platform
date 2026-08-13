# India Data Intelligence Platform

An analytics project built around published Indian government datasets and official government-reported extracts.

## Data included
- Road accidents — Ministry of Road Transport & Highways (2024)
- Weather — India Meteorological Department (all-India southwest monsoon, 2020–2024)
- Air quality — MoEFCC/CPCB government-reported annual PM10 values (2023–24, selected West Bengal cities)
- Population — Census of India (2011)
- Vehicles — Vahan Portal / Ministry of Heavy Industries (registered EVs through FY 2024–25)

**Important:** The CSV files in this repository are real published/government-reported values, not synthetic demo data. The coverage year differs by dataset because government sources release different series on different schedules.

## Folder structure
```text
data/
  raw/
    road_accidents/
    weather/
    air_quality/
    population/
    vehicles/
  processed/
notebooks/
src/
streamlit_app/
sql/
powerbi/
tests/
```

## Sources
1. MoRTH, Road Accidents in India 2024: https://morth.gov.in/
2. Open Government Data Platform India: https://data.gov.in/
3. Census of India: https://censusindia.gov.in/
4. IMD: https://mausam.imd.gov.in/
5. CPCB: https://cpcb.nic.in/
6. Vahan / Ministry of Heavy Industries: https://heavyindustries.gov.in/

## Run the Streamlit app
```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

## Note
Before making analytical claims, check the source period and unit of each dataset. Do not treat the Census 2011 population as a current population estimate.