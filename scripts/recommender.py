"""
Simple mutual fund recommendation system based on risk profile and Sharpe Ratio.
"""

import pandas as pd

scorecard = pd.read_csv("reports/day4_fund_scorecard.csv")
fund_master = pd.read_csv("data/processed/01_fund_master_cleaned.csv")

risk_map = {
    "Low":["Low","Low to Moderate"],
    "Moderate":["Moderate"],
    "High":["Moderately High","High","Very High"]
}

risk = input("Enter Risk Level (Low/Moderate/High): ")

df = scorecard.merge(
    fund_master[
        [
            "amfi_code",
            "scheme_name",
            "risk_category"
        ]
    ],
    on="amfi_code"
)

result = (
    df[
        df["risk_category"]
        .isin(risk_map[risk])
    ].sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3))

print(result[["scheme_name","risk_category","sharpe_ratio"]])