import streamlit as st
import pandas as pd
import sqlite3

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="DashIQ Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("data/cleaned/dashiq.db")
    df = pd.read_sql("SELECT * FROM fact_sales", conn)
    conn.close()
    return df

df = load_data()

# -----------------------------
# HEADER
# -----------------------------
st.title("📊 DashIQ — Sales Dashboard")

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()
total_orders = df["Order ID"].nunique()
profit_margin = total_profit / total_revenue

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("Margin", f"{profit_margin:.2%}")

# -----------------------------
# SAMPLE TABLE
# -----------------------------
st.subheader("Sample Data")
st.dataframe(df.head())