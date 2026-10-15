import streamlit as st
import pandas as pd

df = pd.read_csv("/content/archive.zip")
st.set_page_config(page_title="Netflix Recommendation Dashboard", layout="wide")

st.title("Netflix Recommendation Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("release_year")
st.line_chart(df["release_year"].value_counts().sort_index())

st.subheader("Movies vs TV_Shows")
st.bar_chart(df["type"].value_counts())

# Code to trigger the download
from google.colab import files
files.download("app.py")
