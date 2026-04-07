# DashIQ — Initial Data Inspection Notes

## Dataset
sales_records.csv

## Inspection Objective
To understand the structure and quality of the raw sales dataset before cleaning and analysis.

## Findings

### 1. Dataset Loaded Successfully
The dataset was opened in Python using Pandas.

### 2. Row and Column Count
- Rows: 1,000,000
- Columns: 14

### 3. Sample Records Preview
The dataset contains transactional sales records including:
- Region
- Country
- Item Type
- Sales Channel
- Order Priority
- Order Date
- Order ID
- Ship Date
- Units Sold
- Unit Price
- Unit Cost
- Total Revenue
- Total Cost
- Total Profit

### 4. Data Types
- Text / categorical fields are stored as object
- Numeric fields are stored as int64 / float64
- Order Date and Ship Date were converted to datetime

### 5. Date Range
- Order Date: 2010 to 2017
- Ship Date: 2010 to 2017

## Initial Conclusion
The dataset is structurally suitable for the DashIQ Sales & Revenue Analytics Dashboard and is ready for the next step: Data Quality Assessment.