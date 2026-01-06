import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="T-Beam Lab Diagnostics", page_icon="🧪")

# Pull credentials from the secrets file we created
try:
    lab_ssid = st.secrets["wifi"]["ssid"]
    lab_lat = st.secrets["lab_location"]["latitude"]
    lab_lon = st.secrets["lab_location"]["longitude"]
except:
    st.error("Secrets.toml not found or incorrectly formatted.")
    st.stop()

# --- UI DISPLAY ---
st.title("🧪 Hardware Lab: Franklin, NC")
st.markdown(f"**Connected to:** `{lab_ssid}`")

# Metrics for Hardware Performance
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Lab Latitude", lab_lat)
with c2:
    st.metric("Lab Longitude", lab_lon)
with c3:
    st.metric("GPS Status", "Fix Confirmed", delta="Active")

# Telemetry Log
st.subheader("📡 Live Telemetry Log")
if 'log' not in st.session_state:
    st.session_state.log = []

# Mock button to test UI response
if st.button("Manual Hardware Ping"):
    st.session_state.log.insert(0, {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Event": "Handshake Success",
        "Lat": lab_lat,
        "Lon": lab_lon
    })

st.table(pd.DataFrame(st.session_state.log))
