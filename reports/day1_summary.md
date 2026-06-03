# Day 1 Summary Report

## Fund Master Exploration

### Fund Houses Identified (10)

1. SBI Mutual Fund
2. HDFC Mutual Fund
3. ICICI Prudential MF
4. Nippon India MF
5. Kotak Mahindra MF
6. Axis Mutual Fund
7. Aditya Birla Sun Life MF
8. UTI Mutual Fund
9. Mirae Asset MF
10. DSP Mutual Fund

### Categories

* Equity
* Debt

### Sub-Categories

* Large Cap
* Small Cap
* Mid Cap
* Flexi Cap
* Value
* Large & Mid Cap
* ELSS
* Index
* Index/ETF
* Gilt
* Liquid
* Short Duration

### Risk Categories

* Low
* Moderate
* Moderately High
* High
* Very High

### SEBI Category Codes

* EC01
* EC02
* EC03
* EC04
* EC05
* EC06
* EI01
* DC01
* DC02

---

## AMFI Code Validation

Validation was performed between:

* 01_fund_master.csv
* 02_nav_history.csv

Results:

* Fund Master Codes: 40
* NAV History Codes: 40
* Missing Codes: 0

Conclusion:

All AMFI codes present in the Fund Master dataset exist in the NAV History dataset. Therefore, referential integrity is maintained and datasets can be safely joined using AMFI code.

---

## Live NAV Data Collection

MFAPI integration was successfully tested.

Endpoint Used:

https://api.mfapi.in/mf/125497

The API returned valid historical NAV data and the response was successfully stored as a CSV file for future ETL processing.

---

## Day 1 Completion Status

✅ Project Structure Created

✅ Git Repository Initialized

✅ Dependencies Installed

✅ Data Ingestion Completed

✅ Data Quality Assessment Completed

✅ Fund Master Exploration Completed

✅ AMFI Validation Completed

✅ MFAPI Integration Completed

Day 1 deliverables have been successfully completed and the project is ready for Day 2 (Data Cleaning and SQLite Database Creation).
