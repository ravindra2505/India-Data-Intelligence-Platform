# Power BI Dashboard Plan

## Dashboard Pages

### 1. Executive Overview
- Total road accidents
- Total fatalities
- Total injuries
- EV registrations
- State accident ranking
- Data-domain coverage

### 2. Road Safety Analytics
- Accidents by State/UT
- Fatalities by State/UT
- Fatality rate
- Accidents per 100,000 population
- Top 10 high-risk states

### 3. Environment Analytics
- PM10 by state/region
- Average PM10
- Actual vs normal rainfall
- Rainfall deviation percentage

### 4. Demographics & Mobility
- Population by State/UT
- EV registration trend
- Population vs accidents
- EV growth KPI

## Recommended Data Model

Use the CSV files under `data/raw/` as source tables. Standardize state names and data types before creating relationships. Use state/year keys where the datasets overlap.

## Recommended DAX Measures

```DAX
Total Accidents = SUM(road_accidents[road_accidents])
Total Fatalities = SUM(road_accidents[persons_killed])
Total Injuries = SUM(road_accidents[persons_injured])
Fatality Rate % = DIVIDE([Total Fatalities], [Total Accidents], 0) * 100
```

## Build Order
1. Load road accident, population, weather, air-quality and vehicle CSVs.
2. Clean data types and state names.
3. Create relationships / lookup tables.
4. Add KPI cards.
5. Add state ranking and trend visuals.
6. Add slicers for state/year where applicable.
7. Publish the dashboard and save screenshots in `screenshots/`.

## Resume-Level Outcome
The Power BI layer demonstrates KPI design, data modeling, DAX, cross-domain analysis and decision-support visualization.

> Note: This repository contains the Power BI specification and source datasets. The `.pbix` file must be created locally in Power BI Desktop and then added to the repository if desired.
