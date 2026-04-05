# DashIQ

## Short Project Description
**DashIQ** is a **Sales & Revenue Analytics Dashboard** that transforms raw business data into clear, interactive insights.  
It helps analyze **sales performance, revenue trends, customer behavior, and key business metrics** through a user-friendly dashboard interface.

This project is a **portfolio-ready demonstration** of skills in **data cleaning, analysis, dashboard development, and deployment**, showcasing an end-to-end analytics workflow.

---

## Tools / Tech Stack
- **Python** – main programming language for data processing and analytics  
- **Pandas** – data cleaning, transformation, and analysis  
- **SQLite** – lightweight relational database for structured data storage  
- **Streamlit** – interactive dashboard web application framework  
- **Plotly** – interactive charts, graphs, and visualizations  
- **GitHub** – version control, repository hosting, and documentation  
- **Streamlit Community Cloud** – free deployment and public hosting  

---

## Project Structure
The DashIQ project follows a **structured local development setup** to keep files organized and maintain a scalable workflow throughout the dashboard development process.

```bash
DashIQ/
│
├── app/
│   ├── app.py               # Main Streamlit dashboard application
│   ├── utils.py             # Reusable helper functions
│   ├── charts.py            # Chart and visualization logic
│   ├── data_loader.py       # Data loading and preprocessing functions
│
├── data/
│   ├── raw/                 # Original source datasets
│   ├── cleaned/             # Cleaned and transformed datasets
│
├── docs/
│   ├── project_notes.md     # Development notes and planning
│   ├── scope_document.md    # Project scope and boundaries
│   ├── kpi_definition.md    # KPI definitions and metric descriptions
│
├── sql/
│   ├── queries.sql          # SQL queries for reporting and analysis
│
├── notebooks/
│   ├── data_cleaning.ipynb  # Data cleaning and preparation notebook
│   ├── eda.ipynb            # Exploratory Data Analysis notebook
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignored files