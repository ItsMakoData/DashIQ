# DashIQ — Data Dictionary v1

## Dataset
1000000 Sales Records.csv

## Purpose
This dataset will be used to build the DashIQ Sales & Revenue Analytics Dashboard.

## Columns

| Column Name    |Data Type| Nullable? | Description                               | Business Use            |
|----------------|---------|-----------|-------------------------------------------|-------------------------|
| Region         | String  | No        | Geographic region where the order belongs | Regional sales analysis |
| Country        | String  | No        | Country where the order was placed        | Country performance     |
| Item Type      | String  | No        | Product category sold                     | Category analysis       |
| Sales Channel  | String  | No        | Online or Offline sales channel           | Channel performance     |
| Order Priority | String  | No        | Order urgency level                       | Operational insights    |
| Order Date     | Date    | No        | Date of order placement                   | Sales trend analysis    |
| Order ID       | String  | No        | Unique order identifier                   | Order counting          |
| Ship Date      | Date    | No        | Date order was shipped                    | Shipping analysis       |
| Units Sold     | Integer | No        | Quantity sold                             | Volume analysis         |
| Unit Price     | Float   | No        | Price per unit                            | Pricing analysis        |
| Unit Cost      | Float   | No        | Cost per unit                             | Cost analysis           |
| Total Revenue  | Float   | No        | Total sales amount                        | Revenue KPI             |
| Total Cost     | Float   | No        | Total order cost                          | Cost KPI                |
| Total Profit   | Float   | No        | Total profit amount                       | Profit KPI              |