from pathlib import Path
import pandas as pd

# Get the script directory and navigate to data/raw folder
SCRIPT_DIR = Path(__file__).parent.absolute()
fund_master = pd.read_csv(SCRIPT_DIR.parent / "data" / "raw" / "01_fund_master.csv")

print("\n========== FUND HOUSES ==========\n")
print(fund_master["fund_house"].unique())

print("\nTotal Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\n========== CATEGORIES ==========\n")
print(fund_master["category"].unique())

print("\n========== SUB-CATEGORIES ==========\n")
print(fund_master["sub_category"].unique())

print("\n========== RISK CATEGORIES ==========\n")
print(fund_master["risk_category"].unique())

print("\n========== SEBI CATEGORY CODES ==========\n")
print(fund_master["sebi_category_code"].unique())