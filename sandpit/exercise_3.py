import streamlit as st
import pandas as pd

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

# put some stuff in the tabs to check they are working
with tab1:
    st.dataframe(demo_df)

with tab2:
    st.write("And this is tab two!")
