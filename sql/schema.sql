CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
plan TEXT,
fund_manager TEXT,
risk_category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav (
amfi_code INTEGER,
date DATE,
nav REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
investor_id TEXT,
transaction_date DATE,
amfi_code INTEGER,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
beta REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
fund_house TEXT,
date DATE,
aum_crore REAL
);
