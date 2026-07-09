import os
import sys
from datetime import datetime

import pandas as pd
import streamlit as st

# Allow the dashboard to import files from the src folder
sys.path.append("src")

# Load API key from Streamlit Secrets when deployed online
try:
    if "OPENWEATHER_API_KEY" in st.secrets:
        os.environ["OPENWEATHER_API_KEY"] = st.secrets["OPENWEATHER_API_KEY"]
except Exception:
    pass

from config import COUNTY_LOCATIONS
from fetch_weather import fetch_location_weather
from transform_data import transform_weather_data


st.set_page_config(
    page_title="Kenya County Weather Risk Dashboard",
    page_icon="🌦️",
    layout="wide"
)


@st.cache_data(ttl=900)
def load_weather_data():
    """
    Fetch live weather data and transform it into a risk-scored dataframe.
    Cache refreshes every 15 minutes.
    """

    weather_records = []
    failed_locations = []

    for item in COUNTY_LOCATIONS:
        county = item["county"]
        location = item["location"]

        try:
            record = fetch_location_weather(county, location)
            weather_records.append(record)

        except Exception as error:
            failed_locations.append({
                "county": county,
                "location": location,
                "error": str(error)
            })

    if not weather_records:
        return pd.DataFrame(), failed_locations

    df = transform_weather_data(weather_records)
    return df, failed_locations


st.title("🌦️ Kenya County Weather Risk Dashboard")

st.write(
    "This dashboard fetches live weather data from the OpenWeather API, "
    "calculates weather risk scores for Kenyan counties, and presents "
    "the findings in an interactive online dashboard."
)

if st.button("🔄 Refresh latest weather data"):
    st.cache_data.clear()
    st.rerun()

df, failed_locations = load_weather_data()

if df.empty:
    st.error("No weather data was fetched. Please check the API key or API connection.")
    st.stop()

latest_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.caption(f"Last dashboard refresh: {latest_time}")

total_counties = len(df)
high_risk = len(df[df["risk_level"] == "High"])
medium_risk = len(df[df["risk_level"] == "Medium"])
low_risk = len(df[df["risk_level"] == "Low"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Counties Monitored", total_counties)
col2.metric("High Risk", high_risk)
col3.metric("Medium Risk", medium_risk)
col4.metric("Low Risk", low_risk)

st.divider()

st.subheader("Risk Summary by Level")

risk_summary = (
    df["risk_level"]
    .value_counts()
    .reindex(["Low", "Medium", "High"], fill_value=0)
)

st.bar_chart(risk_summary)

st.subheader("Top Counties by Weather Risk Score")

top_risk = df.sort_values(by="risk_score", ascending=False).head(10)

st.dataframe(
    top_risk[
        [
            "county",
            "location_used",
            "temperature",
            "humidity",
            "wind_speed",
            "weather_description",
            "risk_score",
            "risk_level",
            "timestamp"
        ]
    ],
    use_container_width=True
)

st.subheader("County-Level Weather Risk Data")

selected_risk = st.multiselect(
    "Filter by risk level",
    options=["Low", "Medium", "High"],
    default=["Low", "Medium", "High"]
)

filtered_df = df[df["risk_level"].isin(selected_risk)]

st.dataframe(
    filtered_df[
        [
            "county",
            "location_used",
            "country",
            "temperature",
            "feels_like",
            "humidity",
            "pressure",
            "wind_speed",
            "weather_main",
            "weather_description",
            "risk_score",
            "risk_level",
            "timestamp"
        ]
    ],
    use_container_width=True
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download filtered CSV",
    data=csv,
    file_name="kenya_county_weather_risk_dashboard.csv",
    mime="text/csv"
)

if failed_locations:
    st.warning(f"{len(failed_locations)} locations failed during API lookup.")

    with st.expander("View failed locations"):
        st.dataframe(pd.DataFrame(failed_locations), use_container_width=True)

st.divider()

st.markdown(
    """
    **Project Skills Demonstrated:** API integration, Python automation, data transformation,
    secure API key handling, GitHub Actions, and dashboard reporting.
    """
)