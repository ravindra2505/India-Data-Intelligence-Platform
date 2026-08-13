import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="India Data Intelligence Platform", layout="wide")
st.title("India Data Intelligence Platform")

road = pd.read_csv(ROOT / "data/raw/road_accidents/road_accidents_2024.csv")
st.metric("India road accidents (2024)", f"{road.loc[road.state_ut.eq('All India'),'road_accidents'].iloc[0]:,}")
st.subheader("Road accidents by State/UT — 2024")
st.dataframe(road[road.state_ut.ne("All India")].sort_values("road_accidents", ascending=False), use_container_width=True)