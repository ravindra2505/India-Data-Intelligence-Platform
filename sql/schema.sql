-- India Data Intelligence Platform
-- SQL analytics schema for government-data datasets

DROP TABLE IF EXISTS road_accidents;
DROP TABLE IF EXISTS population;
DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS weather;
DROP TABLE IF EXISTS air_quality;

CREATE TABLE road_accidents (
    state_ut TEXT NOT NULL,
    year INTEGER NOT NULL,
    road_accidents INTEGER,
    persons_killed INTEGER,
    persons_injured INTEGER
);

CREATE TABLE population (
    state_ut TEXT NOT NULL,
    census_year INTEGER NOT NULL,
    population INTEGER
);

CREATE TABLE vehicles (
    financial_year TEXT NOT NULL,
    registered_evs_lakh REAL,
    source_portal TEXT
);

CREATE TABLE weather (
    year INTEGER,
    region TEXT,
    actual_rainfall_mm REAL,
    normal_rainfall_mm REAL
);

CREATE TABLE air_quality (
    state_ut TEXT,
    year TEXT,
    pm10 REAL
);

-- KPI 1: Total road accidents by state
SELECT state_ut, SUM(road_accidents) AS total_accidents
FROM road_accidents
WHERE state_ut <> 'All India'
GROUP BY state_ut
ORDER BY total_accidents DESC;

-- KPI 2: Top 10 states by fatalities
SELECT state_ut, SUM(persons_killed) AS total_fatalities
FROM road_accidents
WHERE state_ut <> 'All India'
GROUP BY state_ut
ORDER BY total_fatalities DESC
LIMIT 10;

-- KPI 3: Injury-to-accident ratio
SELECT state_ut,
       ROUND(100.0 * SUM(persons_injured) / NULLIF(SUM(road_accidents), 0), 2) AS injuries_per_100_accidents
FROM road_accidents
WHERE state_ut <> 'All India'
GROUP BY state_ut
ORDER BY injuries_per_100_accidents DESC;

-- KPI 4: Population ranking
SELECT state_ut, population
FROM population
ORDER BY population DESC;

-- KPI 5: EV registration trend
SELECT financial_year, registered_evs_lakh
FROM vehicles
ORDER BY financial_year;

-- KPI 6: EV growth between available periods
SELECT MIN(financial_year) AS first_year,
       MAX(financial_year) AS latest_year,
       ROUND(100.0 * (MAX(registered_evs_lakh) - MIN(registered_evs_lakh)) /
             NULLIF(MIN(registered_evs_lakh), 0), 2) AS growth_percent
FROM vehicles;

-- KPI 7: Weather rainfall deviation
SELECT year, region,
       actual_rainfall_mm,
       normal_rainfall_mm,
       ROUND(actual_rainfall_mm - normal_rainfall_mm, 2) AS deviation_mm,
       ROUND(100.0 * (actual_rainfall_mm - normal_rainfall_mm) /
             NULLIF(normal_rainfall_mm, 0), 2) AS deviation_percent
FROM weather;

-- KPI 8: Air quality ranking
SELECT state_ut, AVG(pm10) AS avg_pm10
FROM air_quality
GROUP BY state_ut
ORDER BY avg_pm10 DESC;
