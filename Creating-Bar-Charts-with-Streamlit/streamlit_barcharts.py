import streamlit as st
import pandas as pd
import altair as alt

st.write("Built-in Bar chart")
"Energy Costs By Month"
chart_data = pd.DataFrame([10,13, 11],columns=["Energy Costs"])
st.bar_chart(chart_data)

st.write("Altair Chart with Axis Labels")

source = pd.DataFrame({
        'Price ($)': [10, 15, 20],
        'Month': ['January', 'February', 'March']
    })

bar_chart = alt.Chart(source).mark_bar().encode(
    y='Price ($)',
    x='Month',
)
st.altair_chart(bar_chart, use_container_width=True)

st.write("Altair Chart With Stacked Bars")

source = pd.DataFrame({
"EnergyType": ["Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas"],
"Price ($)":  [150,73,15,130,80,20,170,83,20],
"Date": ["2022-1-23", "2022-1-30","2022-1-5","2022-2-21", "2022-2-1","2022-2-1","2022-3-1","2022-3-1","2022-3-1"]
})

bar_chart = alt.Chart(source).mark_bar().encode(
    x="month(Date):O",
    y="sum(Price ($)):Q",
    color="EnergyType:N"
)
st.altair_chart(bar_chart, use_container_width=True)

st.write("Altair Bar Chart Horizontal")

source = pd.DataFrame({
"EnergyType": ["Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas","Electricity","Gasoline","Natural Gas"],
"Price ($)":  [150,73,15,130,80,20,170,83,20],
"Date": ["2022-1-23", "2022-1-30","2022-1-5","2022-2-21", "2022-2-1","2022-2-1","2022-3-1","2022-3-1","2022-3-1"]
})

bar_chart = alt.Chart(source).mark_bar().encode(
    y="month(Date):O",
    x="sum(Price ($)):Q",
    color="EnergyType:N"
)
st.altair_chart(bar_chart, use_container_width=True)

st.write("Altair Bar Chart Sort")

source = pd.DataFrame({
    "Price ($)": [10, 15, 20],
    "Month": ["January", "February", "March"]

    })

bar_chart = alt.Chart(source).mark_bar().encode(
    x="sum(Price ($)):Q",
    y=alt.Y("Month:N", sort="-x")
)

st.altair_chart(bar_chart, use_container_width=True)

