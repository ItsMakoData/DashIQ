-- ===============================
-- DashIQ KPI Queries
-- ===============================

-- Total Revenue
SELECT SUM("Total Revenue") AS total_revenue FROM fact_sales;

-- Total Profit
SELECT SUM("Total Profit") AS total_profit FROM fact_sales;

-- Total Orders
SELECT COUNT(DISTINCT "Order ID") AS total_orders FROM fact_sales;

-- Average Order Value
SELECT SUM("Total Revenue") * 1.0 / COUNT(DISTINCT "Order ID") AS avg_order_value FROM fact_sales;

-- Profit Margin
SELECT SUM("Total Profit") * 1.0 / SUM("Total Revenue") AS profit_margin FROM fact_sales;

-- Top Product
SELECT "Item Type", SUM("Total Revenue") AS total_revenue
FROM fact_sales
GROUP BY "Item Type"
ORDER BY total_revenue DESC;

-- Best Region
SELECT Region, SUM("Total Profit") AS total_profit
FROM fact_sales
GROUP BY Region
ORDER BY total_profit DESC;