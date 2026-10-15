
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Netflix Recommendation Dashboard",
    layout="wide"
)

df = pd.read_csv("archive.zip")

st.title("🎬 Netflix Content Analytics Dashboard")
st.write("Explore Netflix movies and TV shows through interactive visualizations.")

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# Prepare columns
df["release_year"] = pd.to_numeric(
    df["release_year"], errors="coerce"
)
df["date_added"] = pd.to_datetime(
    df["date_added"], errors="coerce"
)

# Chart 1: Movies vs TV Shows
st.subheader("1. Movies vs TV Shows")
type_counts = df["type"].value_counts()
fig1 = px.pie(
    names=type_counts.index,
    values=type_counts.values,
    hole=0.5,
    title="Content Type Distribution"
)
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Top countries
st.subheader("2. Top 10 Countries")
countries = (
    df["country"].dropna().astype(str)
    .str.split(",").explode().str.strip()
)
top_countries = countries.value_counts().head(10).sort_values()
fig2 = px.bar(
    x=top_countries.values,
    y=top_countries.index,
    orientation="h",
    labels={"x": "Number of Titles", "y": "Country"},
    title="Top Countries by Titles"
)
st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Top genres
st.subheader("3. Top 10 Genres")
genres = (
    df["listed_in"].dropna().astype(str)
    .str.split(",").explode().str.strip()
)
top_genres = genres.value_counts().head(10).sort_values()
fig3 = px.bar(
    x=top_genres.values,
    y=top_genres.index,
    orientation="h",
    title="Most Common Genres",
    labels={"x": "Number of Titles", "y": "Genre"}
)
st.plotly_chart(fig3, use_container_width=True)

# Chart 4: Content ratings
st.subheader("4. Content Ratings")
ratings = df["rating"].dropna().value_counts().head(10)
fig4 = px.pie(
    names=ratings.index,
    values=ratings.values,
    title="Rating Distribution"
)
st.plotly_chart(fig4, use_container_width=True)

# Chart 5: Movie duration histogram
st.subheader("5. Movie Duration")
minutes = pd.to_numeric(
    df.loc[df["type"] == "Movie", "duration"]
    .astype(str).str.extract(r"(\d+)\s*min", expand=False),
    errors="coerce"
).dropna()

fig5 = px.histogram(
    x=minutes,
    nbins=30,
    labels={"x": "Duration in Minutes"},
    title="Movie Runtime Distribution"
)
st.plotly_chart(fig5, use_container_width=True)

# Chart 6: Titles released by year
st.subheader("6. Titles Released by Year")
year_counts = df["release_year"].dropna().value_counts().sort_index()
fig6 = px.line(
    x=year_counts.index,
    y=year_counts.values,
    markers=True,
    labels={"x": "Release Year", "y": "Number of Titles"},
    title="Release Trend"
)
st.plotly_chart(fig6, use_container_width=True)

# Chart 7: Content added over time
st.subheader("7. Content Added Over Time")
added = df.dropna(subset=["date_added"]).copy()
added["year_added"] = added["date_added"].dt.year
added_counts = added["year_added"].value_counts().sort_index()

fig7 = px.area(
    x=added_counts.index,
    y=added_counts.values,
    labels={"x": "Year Added", "y": "Number of Titles"},
    title="Netflix Content Added by Year"
)
st.plotly_chart(fig7, use_container_width=True)
