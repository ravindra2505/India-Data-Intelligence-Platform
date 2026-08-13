-- Starter SQL schema for the verified government-data extracts
CREATE TABLE road_accidents (
    state_ut TEXT,
    year INTEGER,
    road_accidents INTEGER
);

CREATE TABLE population (
    state_ut TEXT,
    census_year INTEGER,
    population INTEGER
);

CREATE TABLE vehicles (
    financial_year TEXT,
    registered_evs_lakh REAL,
    source_portal TEXT
);