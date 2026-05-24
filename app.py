from scraper import get_jobs
from api import get_exchange_rates
import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")
df = load_data()

# Sidebar filters
region = st.sidebar.multiselect("Region", df["Region"].unique())
category = st.sidebar.multiselect("Category", df["Category"].unique())

if region: df = df[df["Region"].isin(region)]
if category: df = df[df["Category"].isin(category)]

# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Orders", df.shape[0])
# 1. Monthly sales trend
monthly = df.groupby("Month")["Sales"].sum().reset_index()
st.plotly_chart(px.line(monthly, x="Month", y="Sales", title="Monthly Revenue"))

# 2. Sales by Category
cat = df.groupby("Category")["Sales"].sum().reset_index()
st.plotly_chart(px.bar(cat, x="Category", y="Sales", color="Category"))

# 3. Profit heatmap by Region+Category
pivot = df.pivot_table(values="Profit", index="Region", columns="Category")
fig = px.imshow(pivot, text_auto=True, title="Profit by Region & Category", color_continuous_scale="RdYlGn")
st.plotly_chart(fig)
# Live Currency Rates Widget
st.subheader("💱 Live Currency Exchange Rates (USD Base)")

rates = get_exchange_rates()

# Show only selected currencies
selected = ["INR", "EUR", "GBP", "JPY", "AUD"]
col1, col2, col3, col4, col5 = st.columns(5)
cols = [col1, col2, col3, col4, col5]

for i, currency in enumerate(selected):
    cols[i].metric(label=currency, value=round(rates[currency], 2))
# Job Postings Section
st.subheader("💼 Live Python Job Postings (Remote)")

keyword = st.selectbox("Search jobs by keyword", ["python", "data-analyst", "sql", "streamlit"])

jobs = get_jobs(keyword)

if jobs:
    for job in jobs:
        with st.expander(f"{job['Title']} — {job['Company']}"):
            st.write(f"🏷️ Tags: {job['Tags']}")
            st.markdown(f"[View Job]({job['Link']})")
else:
    st.write("No jobs found. Try a different keyword.")    