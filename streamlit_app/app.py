import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"

st.set_page_config(page_title="India Data Intelligence Platform", page_icon="🇮🇳", layout="wide")
st.title("🇮🇳 India Data Intelligence Platform")
st.caption("Government-data analytics and decision-support dashboard")

@st.cache_data
def load_data():
    return (
        pd.read_csv(DATA / "road_accidents" / "road_accidents_2024.csv"),
        pd.read_csv(DATA / "weather" / "imd_monsoon_2020_2024.csv"),
        pd.read_csv(DATA / "air_quality" / "cpcb_pm10_2023_24_west_bengal.csv"),
        pd.read_csv(DATA / "population" / "census_2011_state_population.csv"),
        pd.read_csv(DATA / "vehicles" / "vahan_registered_evs_2019_20_2024_25.csv"),
    )

road, weather, air, population, vehicles = load_data()

page = st.sidebar.radio("Dashboard", ["Overview", "Road Safety", "Environment", "Demographics & Mobility", "Data Explorer"])

if page == "Overview":
    st.header("Executive Overview")
    all_india = road[road["state_ut"].eq("All India")]
    accidents = int(all_india["road_accidents"].iloc[0]) if not all_india.empty else 0
    deaths = int(all_india["persons_killed"].iloc[0]) if "persons_killed" in road.columns and not all_india.empty else 0
    injured = int(all_india["persons_injured"].iloc[0]) if "persons_injured" in road.columns and not all_india.empty else 0
    ev_total = float(vehicles["registered_evs_lakh"].sum()) if "registered_evs_lakh" in vehicles.columns else 0
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Road accidents", f"{accidents:,}")
    c2.metric("Persons killed", f"{deaths:,}")
    c3.metric("Persons injured", f"{injured:,}")
    c4.metric("EV registrations (lakh)", f"{ev_total:,.2f}")
    st.divider()
    st.subheader("Platform data coverage")
    coverage = pd.DataFrame({"Domain": ["Road Safety", "Weather", "Air Quality", "Population", "Vehicles"], "Rows": [len(road), len(weather), len(air), len(population), len(vehicles)]})
    st.bar_chart(coverage.set_index("Domain"))

elif page == "Road Safety":
    st.header("🚗 Road Safety Analytics")
    states = road[road["state_ut"].ne("All India")].sort_values("road_accidents", ascending=False).copy()
    c1, c2, c3 = st.columns(3)
    c1.metric("States/UTs", len(states))
    c2.metric("Highest accidents", states.iloc[0]["state_ut"] if len(states) else "N/A")
    c3.metric("Highest accident count", f"{int(states.iloc[0]['road_accidents']):,}" if len(states) else "0")
    st.subheader("Top 15 States/UTs by accidents")
    st.bar_chart(states.set_index("state_ut")["road_accidents"].head(15))
    st.dataframe(states, use_container_width=True, hide_index=True)

elif page == "Environment":
    st.header("🌱 Environment Analytics")
    c1, c2 = st.columns(2)
    c1.metric("Air-quality records", len(air))
    c2.metric("Weather records", len(weather))
    st.subheader("Air Quality — PM10")
    st.dataframe(air, use_container_width=True, hide_index=True)
    if "pm10" in air.columns:
        st.bar_chart(air.set_index(air.columns[0])["pm10"])
    st.subheader("Weather / Monsoon Data")
    st.dataframe(weather, use_container_width=True, hide_index=True)

elif page == "Demographics & Mobility":
    st.header("👥 Demographics & Mobility")
    c1, c2 = st.columns(2)
    c1.metric("Population records", len(population))
    c2.metric("Vehicle records", len(vehicles))
    st.subheader("State Population — Census 2011")
    st.dataframe(population, use_container_width=True, hide_index=True)
    if "population" in population.columns:
        st.bar_chart(population.set_index(population.columns[0])["population"].sort_values(ascending=False).head(15))
    st.subheader("Registered EVs")
    st.dataframe(vehicles, use_container_width=True, hide_index=True)
    if "registered_evs_lakh" in vehicles.columns:
        st.line_chart(vehicles.set_index(vehicles.columns[0])["registered_evs_lakh"])

else:
    st.header("🔎 Data Explorer")
    dataset = st.selectbox("Choose dataset", ["Road Accidents", "Weather", "Air Quality", "Population", "Vehicles"])
    selected = {"Road Accidents": road, "Weather": weather, "Air Quality": air, "Population": population, "Vehicles": vehicles}[dataset]
    st.write(f"**{len(selected):,} rows × {len(selected.columns):,} columns**")
    st.dataframe(selected, use_container_width=True, hide_index=True)

st.sidebar.divider()
st.sidebar.caption("Built with Python • Pandas • Streamlit")
