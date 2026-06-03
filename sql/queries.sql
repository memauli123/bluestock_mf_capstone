-- 1.Top 5 funds by AUM

SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- 2.Average NAV by month

SELECT strftime('%Y-%m', date) AS month,
       AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- 3.SIP Inflow Growth

SELECT month,
       sip_inflow_crore,
       yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- 4.Transactions by State

SELECT state,
       COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 5.Funds with Expense Ratio < 1%

SELECT scheme_name,
       expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6.Average Sharpe Ratio by Fund House

SELECT fund_house,
       AVG(sharpe_ratio) AS avg_sharpe
FROM scheme_performance
GROUP BY fund_house;

-- 7.Top 10 Funds by 5-Year Return

SELECT scheme_name,
       return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8.Investor Count by Gender

SELECT gender,
       COUNT(*) AS investor_count
FROM investor_transactions
GROUP BY gender;

-- 9.Portfolio Holdings by Sector

SELECT sector,
       COUNT(*) AS holdings
FROM portfolio_holdings
GROUP BY sector
ORDER BY holdings DESC;

-- 10.Average Beta by Risk Grade

SELECT risk_grade,
       AVG(beta) AS avg_beta
FROM scheme_performance
GROUP BY risk_grade;