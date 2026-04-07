# DashIQ — Duplicate Record Report

## Dataset
sales_records.csv

## Objective
To identify duplicate records in the raw dataset and determine whether any rows should be marked for removal.

## Duplicate Check Summary

### 1. Exact Duplicate Rows
A duplicate scan was performed across all columns in the dataset.

- Exact duplicate rows found: [Replace with result]

### 2. Duplicate Order ID Check
A separate check was performed on the `Order ID` field to identify repeated transaction identifiers.

- Repeated Order IDs found: [Replace with result]

### 3. Validation Notes
Duplicate rows were reviewed to determine whether they represent:
- exact repeated records
- valid business records
- rows that should be removed during cleaning

### 4. Handling Strategy
- Exact duplicate rows will be marked for removal
- Repeated `Order ID` values will be reviewed before deletion
- Only confirmed invalid duplicates should be removed

## Initial Conclusion
The dataset [does not contain duplicates / contains duplicate rows / requires duplicate cleanup] and is ready for the next data quality step.