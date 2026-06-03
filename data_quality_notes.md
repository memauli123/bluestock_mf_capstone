# Data Quality Summary – Day 1

## Dataset Overview

A total of 10 datasets were successfully loaded and validated.

| Dataset                  | Rows   | Columns |
| ------------------------ | ------ | ------- |
| 01_fund_master           | 40     | 15      |
| 02_nav_history           | 46,000 | 3       |
| 03_aum_by_fund_house     | 90     | 5       |
| 04_monthly_sip_inflows   | 48     | 6       |
| 05_category_inflows      | 144    | 3       |
| 06_industry_folio_count  | 21     | 6       |
| 07_scheme_performance    | 40     | 19      |
| 08_investor_transactions | 32,778 | 13      |
| 09_portfolio_holdings    | 322    | 8       |
| 10_benchmark_indices     | 8,050  | 3       |

---

## Data Quality Checks Performed

### 1. Missing Values Check

Most datasets contain no missing values.

**Observation:**

* `04_monthly_sip_inflows.csv` contains **12 missing values** in the `yoy_growth_pct` column.
* These missing values are likely present because Year-over-Year growth cannot be calculated for the first 12 months of data.

No other missing values were detected.

---

### 2. Data Type Validation

Several date fields are currently stored as string (`object`) datatype and will require conversion to datetime format during the data cleaning stage.

Columns requiring datetime conversion:

* `launch_date`
* `date`
* `month`
* `transaction_date`
* `portfolio_date`

---

### 3. Numerical Columns

All major numerical fields have been loaded correctly as numeric datatypes:

* NAV values
* Expense ratios
* AUM values
* Portfolio weights
* Returns
* Benchmark values
* Investor transaction amounts

No datatype inconsistencies were observed.

---

### 4. AMFI Code Availability

AMFI scheme codes are available across multiple datasets:

* Fund Master
* NAV History
* Scheme Performance
* Investor Transactions
* Portfolio Holdings

These codes can be used as primary keys for future joins and validation checks.

---

### 5. Initial Observations

* Fund Master contains 40 mutual fund schemes.
* NAV History contains 46,000 historical NAV records.
* Investor Transactions dataset contains 32,778 transactions.
* Benchmark dataset contains 8,050 market index observations.
* Portfolio Holdings dataset contains 322 stock holdings across schemes.

---

## Identified Anomalies

### Minor Issues

1. Missing values in `yoy_growth_pct` (12 records).
2. Date-related columns stored as strings and require conversion.
3. No duplicate records detected during initial inspection.
4. No missing AMFI codes observed.
5. No missing fund house, category, benchmark, or risk category values detected.

---

## Conclusion

The datasets are in good condition and suitable for further ETL processing. The primary cleaning requirements for Day 2 will be:

* Datetime conversion
* AMFI code validation across datasets
* Duplicate checks
* Data consistency checks after joins
* SQLite database loading
