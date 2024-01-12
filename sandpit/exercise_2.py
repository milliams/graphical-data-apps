import streamlit as st

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

# put some text in the tabs to check they are working
with tab1:
    st.write("This text is placed inside the first tab.")

with tab2:
    st.write("This tab will contain stuff later.")
