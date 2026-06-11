# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project analyzes mutual fund industry data using Python, SQLite, and Power BI. The objective is to build a complete data analytics pipeline that covers data ingestion, cleaning, exploratory data analysis, performance evaluation, advanced risk analytics, and interactive dashboard creation.

The project was completed as part of the Bluestock Fintech Capstone Internship Program.

---

## Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Store and manage cleaned data using SQLite.
* Perform exploratory data analysis (EDA).
* Calculate mutual fund performance metrics.
* Conduct advanced risk and investor analytics.
* Create an interactive Power BI dashboard.
* Generate actionable insights and recommendations.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* Power BI
* Git & GitHub

---

## Project Structure

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/

├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── dashboard.pdf
│   ├── page1.png
│   ├── page2.png
│   ├── page3.png
│   └── page4.png

├── data/
│   ├── raw/
│   ├── processed/
│   └── db/

├── notebooks/
│   ├── eda_analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── adv_analysis.ipynb

├── reports/
│   ├── day3_eda_charts/
│   ├── day6_reports&charts/
│   ├── day1_summary.md
│   ├── day2_data_dictionary.md
│   ├── day4_alpha_beta.csv
│   ├── day4_fund_scorecard.csv
│   └── day4_tracking_error.csv

├── scripts/
│   ├── amfi_validation.py
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── fund_master_exploration.py
│   ├── live_nav_fetch.py
│   ├── load_to_sqlite.py
│   ├── recommender.py
│   └── run_pipeline.py

├── sql/
│   ├── schema.sql
│   └── queries.sql

├── .gitignore
├── README.md
└── requirements.txt
```


---

## Datasets Used

1. Fund Master Data
2. Daily NAV Data
3. Investor Transaction Data
4. Portfolio Holdings Data
5. Industry Statistics Data

---

## ETL Pipeline

The ETL process consists of:

1. Data Ingestion
2. Data Validation
3. Data Cleaning
4. Data Transformation
5. Loading into SQLite Database

Scripts used:

* data_ingestion.py
* data_cleaning.py
* load_to_sqlite.py

---

## Exploratory Data Analysis

Key analyses performed:

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trends
* Category Inflow Heatmap
* Investor Demographics Analysis
* Geographic Distribution Analysis
* Folio Growth Analysis
* Return Correlation Analysis
* Sector Allocation Analysis

---

## Performance Analytics

Metrics calculated:

* Daily Returns
* CAGR (1 Year, 3 Year, 5 Year)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard
* Tracking Error

---

## Advanced Analytics

Advanced analyses include:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* Sector Concentration (HHI)

---

## Dashboard

The Power BI dashboard contains four pages:

### Industry Overview

* Total AUM
* SIP Inflows
* Folio Count
* Scheme Count

### Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* Benchmark Comparison

### Investor Analytics

* State-wise Investments
* Age Group Analysis
* Transaction Trends

### SIP & Market Trends

* SIP Inflow Trends
* Category-wise Inflows
* Market Comparison

---

## Key Findings

* Moderate-risk funds achieved strong risk-adjusted returns based on Sharpe Ratio.
* Investor cohorts from 2024 contributed the highest investment volume.
* SIP continuity analysis identified a large number of potentially at-risk investors.
* Several funds showed concentrated sector allocations based on HHI analysis.
* Dashboard visualizations enabled interactive exploration of fund performance and investor behavior.

---


## Deliverables

* ETL Pipeline
* SQLite Database
* EDA Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Report
* Presentation

---

## Author

Mauli Kukreti

B.Tech Computer Science & Engineering

Graphic Era Deemed to be University

Bluestock Fintech Capstone Internship Project
