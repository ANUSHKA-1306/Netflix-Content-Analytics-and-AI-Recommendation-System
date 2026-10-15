import streamlit as st
import pandas as pd

df = pd.read_csv("/content/city_day.csv")

st.set_page_config(page_title="Air Quality Prediction Dashboard", layout="wide")

st.title("🌍 Air Quality Prediction Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("AQI Trend")
st.line_chart(df["AQI"])

st.subheader("PM2.5 vs PM10")
st.bar_chart(df[["PM2.5", "PM10"]])
