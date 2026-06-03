import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)

# NAV HISTORY

nav = pd.read_csv(RAW / "02_nav_history.csv")
print("Original Shape:", nav.shape)

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

# Forward fill NAV within each scheme
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
print("Cleaned Shape:", nav.shape)
nav.to_csv(PROCESSED / "02_nav_history_cleaned.csv", index=False)

print("NAV cleaned successfully")




# INVESTOR TRANSACTIONS

txn = pd.read_csv(RAW / "08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = txn["transaction_type"].str.strip().str.title()

txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]

invalid_kyc = txn[~txn["kyc_status"].isin(valid_kyc)]

print("Invalid KYC rows:", len(invalid_kyc))

txn.to_csv(
    PROCESSED / "08_investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned")




# SCHEME PERFORMANCE
perf = pd.read_csv(RAW / "07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

expense_anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    | (perf["expense_ratio_pct"] > 2.5)
]

print("Expense anomalies:", len(expense_anomalies))

perf.to_csv(
    PROCESSED / "07_scheme_performance_cleaned.csv",
    index=False
)

print("Performance cleaned")


#copy remaining files
other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:
    df = pd.read_csv(RAW / file)
    df.to_csv(PROCESSED / file.replace(".csv", "_cleaned.csv"), index=False)

print("Remaining files copied")