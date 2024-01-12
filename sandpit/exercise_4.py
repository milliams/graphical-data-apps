import streamlit as st
import pandas as pd
import plotly.express as px

# use pandas to read our CSV file into a dataframe called "demo_df"
demo_df = pd.read_csv("demo_dataset.csv")

# build the sidebar
with st.sidebar:
    st.title("World Demographics")

# create two columns, of ratio 3:1
column1, column2 = st.columns([3, 1])

# place info box in first column
with column1:
    st.info("Welcome to the global demographic data explorer app.")

# create two tabs
tab1, tab2 = st.tabs(["Data", "Visualisation"])

# display the dataframe in tab1
with tab1:
    st.dataframe(demo_df)

# build px chart object
chart = px.scatter(
    data_frame=demo_df,
    x="HDI index",
    y="GDP per capita",
    color="Continent",
    size="CO2 per capita",
    hover_name="Country",
)

# display the chart in tab2
with tab2:
    st.plotly_chart(chart)
