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

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

df = load_data()

# Ensure datetime conversion
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -----------------------------
# HEADER
# -----------------------------
st.markdown("# DashIQ Dashboard")
st.markdown("### Sales Performance & Analytics Overview")
st.markdown("---")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filter Panel")

# Date Range Filter
min_date = df["Order Date"].min()
max_date = df["Order Date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Region Filter
regions = sorted(df["Region"].dropna().unique())
selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

# Category Filter
categories = sorted(df["Item Type"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

# Product Filter (Dependent on Category)
filtered_products = df[df["Item Type"].isin(selected_categories)]["Item Type"].unique()
selected_products = st.sidebar.multiselect(
    "Select Product",
    sorted(filtered_products),
    default=filtered_products
)

# Apply Filters
filtered_df = df.copy()

# Date filter
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["Order Date"] >= pd.to_datetime(start_date)) &
        (filtered_df["Order Date"] <= pd.to_datetime(end_date))
    ]

# Region filter
filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]

# Category filter
filtered_df = filtered_df[filtered_df["Item Type"].isin(selected_categories)]

# Product filter
filtered_df = filtered_df[filtered_df["Item Type"].isin(selected_products)]

# Handle Empty Data
if filtered_df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# Reset button and active filters
if st.sidebar.button("Reset Filters"):
    st.rerun()
st.markdown("### Active Filters")
st.write(f"**Date Range:** {date_range[0]} to {date_range[1]}")
st.write(f"**Region:** {', '.join(selected_regions) if selected_regions else 'None'}")
st.write(f"**Category:** {', '.join(selected_categories) if selected_categories else 'None'}")

# ====================================
# KPI CARDS (TASK 26)
# ====================================
st.markdown("## Key Metrics")
st.caption("Overall performance indicators across selected filters")

col1, col2, col3, col4, col5 = st.columns(5)

total_revenue = filtered_df["Total Revenue"].sum()
total_profit = filtered_df["Total Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
aov = total_revenue / total_orders if total_orders != 0 else 0
profit_margin = total_profit / total_revenue if total_revenue != 0 else 0

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("AOV", f"${aov:,.2f}")
col5.metric("Margin", f"{profit_margin:.2%}")

st.markdown("---")

# ====================================
# 📈 SALES TRENDS (TASK 27)
# ====================================
st.markdown("## Sales Trends")
st.caption("Revenue and profit progression over time")

trend_df = filtered_df.groupby(["Year", "Month"], as_index=False).agg({
    "Total Revenue": "sum",
    "Total Profit": "sum"
})

trend_df["Year-Month"] = trend_df["Year"].astype(str) + "-" + trend_df["Month"].astype(str)

st.line_chart(trend_df.set_index("Year-Month")[["Total Revenue", "Total Profit"]])

st.markdown("---")

# ====================================
# 📦 CATEGORY PERFORMANCE (TASK 28)
# ====================================
st.markdown("## Category Performance")
st.caption("Sales and profitability by product category")

col1, col2 = st.columns(2)

category_rev = filtered_df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False)
category_profit = filtered_df.groupby("Item Type")["Total Profit"].sum().sort_values(ascending=False)

with col1:
    st.markdown("### Revenue by Category")
    st.bar_chart(category_rev)

with col2:
    st.markdown("### Profit by Category")
    st.bar_chart(category_profit)

st.markdown("---")

# ====================================
# 🌍 REGIONAL PERFORMANCE (TASK 29)
# ====================================
st.markdown("## Regional Performance")
st.caption("Market performance across different regions")

col1, col2 = st.columns(2)

region_rev = filtered_df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)
region_profit = filtered_df.groupby("Region")["Total Profit"].sum().sort_values(ascending=False)

with col1:
    st.markdown("### Revenue by Region")
    st.bar_chart(region_rev)

with col2:
    st.markdown("### Profit by Region")
    st.bar_chart(region_profit)

st.markdown("---")

# ====================================
# 🛒 PRODUCT PERFORMANCE (TASK 30)
# ====================================
st.markdown("## Product Performance")
st.caption("Top-performing products by revenue and profitability")

col1, col2 = st.columns(2)

top_products_sales = (
    filtered_df.groupby("Item Type")["Total Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products_profit = (
    filtered_df.groupby("Item Type")["Total Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

with col1:
    st.markdown("### Top 10 Products (Revenue)")
    st.bar_chart(top_products_sales)

with col2:
    st.markdown("### Top 10 Products (Profit)")
    st.bar_chart(top_products_profit)

st.markdown("### Product Ranking Table")

product_table = filtered_df.groupby("Item Type").agg({
    "Total Revenue": "sum",
    "Total Profit": "sum",
    "Units Sold": "sum"
}).sort_values("Total Revenue", ascending=False)

st.dataframe(product_table, use_container_width=True)

st.markdown("---")

# ====================================
# 👤 CUSTOMER PERFORMANCE (TASK 31)
# ====================================
st.markdown("## 👤 Customer Performance")

st.info("Customer-level data is not available in the current dataset. Consider collecting customer ID or account information for deeper analysis.")

st.markdown("---")

# ====================================
# 🧠 ANALYST INSIGHTS (TASK 33)
# ====================================
st.markdown("## Analyst Insights")

st.markdown("""
**Key Findings**
• Revenue is driven primarily by a few high-performing categories
• Some regions generate strong revenue but lower profit margins
• High discount segments increase sales but reduce profitability
• Sales show seasonal spikes during certain months

**Recommendations**
• Focus on high-margin categories for sustainable growth
• Optimize pricing strategy in low-margin regions
• Reduce excessive discounting where profit is impacted
• Investigate seasonal demand to plan inventory

**Summary**
The business shows strong revenue performance, but profitability varies across categories and regions. Strategic pricing and cost optimization can significantly improve overall margins.
""")

st.markdown("---")

# ====================================
# ⬇️ EXPORT DATA (TASK 34)
# ====================================
st.markdown("## ⬇Export Data")
st.caption("Download the filtered dataset for external analysis")

csv = convert_df(filtered_df)

st.download_button(
    label="Download Filtered Data (CSV)",
    data=csv,
    file_name="dashiq_filtered_data.csv",
    mime="text/csv",
)

st.markdown("### Filtered Data Preview")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.caption("Dashboard built with Streamlit • Data from DashIQ Dataset")