-- India Data Intelligence Platform — Analytics Queries

-- 1. Highest accident states
SELECT state_ut, road_accidents
FROM road_accidents
WHERE state_ut <> 'All India'
ORDER BY road_accidents DESC
LIMIT 10;

-- 2. Highest fatality states
SELECT state_ut, persons_killed
FROM road_accidents
WHERE state_ut <> 'All India'
ORDER BY persons_killed DESC
LIMIT 10;

-- 3. Accident severity
SELECT state_ut,
       ROUND(100.0 * persons_killed / NULLIF(road_accidents, 0), 2) AS fatality_rate_percent
FROM road_accidents
WHERE state_ut <> 'All India'
ORDER BY fatality_rate_percent DESC;

-- 4. Population vs road accidents
SELECT p.state_ut,
       p.population,
       r.road_accidents,
       ROUND(100000.0 * r.road_accidents / NULLIF(p.population, 0), 2) AS accidents_per_100k_population
FROM population p
JOIN road_accidents r ON LOWER(TRIM(p.state_ut)) = LOWER(TRIM(r.state_ut))
WHERE r.state_ut <> 'All India'
ORDER BY accidents_per_100k_population DESC;

-- 5. EV registration trend
SELECT financial_year, registered_evs_lakh
FROM vehicles
ORDER BY financial_year;

-- 6. Weather deviation
SELECT year, region,
       actual_rainfall_mm - normal_rainfall_mm AS rainfall_deviation_mm
FROM weather
ORDER BY year;

-- 7. Air-quality summary
SELECT state_ut,
       ROUND(AVG(pm10), 2) AS avg_pm10,
       MAX(pm10) AS max_pm10
FROM air_quality
GROUP BY state_ut
ORDER BY avg_pm10 DESC;
