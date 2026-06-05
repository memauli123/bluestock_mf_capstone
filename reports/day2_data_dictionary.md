# Data Dictionary

## 01_fund_master

* amfi_code - Integer - Unique AMFI scheme code
* fund_house - Text - Mutual fund company
* scheme_name - Text - Scheme name
* category - Text - Fund category
* sub_category - Text - Fund sub-category
* plan - Text - Direct/Regular plan
* launch_date - Date - Fund launch date
* benchmark - Text - Benchmark index
* expense_ratio_pct - Float - Expense ratio percentage
* exit_load_pct - Float - Exit load percentage
* min_sip_amount - Integer - Minimum SIP amount
* min_lumpsum_amount - Integer - Minimum lump sum amount
* fund_manager - Text - Fund manager name
* risk_category - Text - Risk category
* sebi_category_code - Text - SEBI category code



## 02_nav_history

* amfi_code - Integer - AMFI scheme code
* date - Date - NAV date
* nav - Float - Net Asset Value



## 03_aum_by_fund_house

* date - Date - Reporting date
* fund_house - Text - Mutual fund company
* aum_lakh_crore - Float - AUM in lakh crore
* aum_crore - Integer - AUM in crore
* num_schemes - Integer - Number of schemes



## 04_monthly_sip_inflows

* month - Text - Reporting month
* sip_inflow_crore - Integer - SIP inflow amount
* active_sip_accounts_crore - Float - Active SIP accounts
* new_sip_accounts_lakh - Float - New SIP accounts
* sip_aum_lakh_crore - Float - SIP AUM
* yoy_growth_pct - Float - Year-over-year growth percentage



## 05_category_inflows

* month - Text - Reporting month
* category - Text - Fund category
* net_inflow_crore - Float - Net inflow amount



## 06_industry_folio_count

* month - Text - Reporting month
* total_folios_crore - Float - Total folios
* equity_folios_crore - Float - Equity folios
* debt_folios_crore - Float - Debt folios
* hybrid_folios_crore - Float - Hybrid folios
* others_folios_crore - Float - Other folios



## 07_scheme_performance

* amfi_code - Integer - AMFI scheme code
* scheme_name - Text - Scheme name
* fund_house - Text - Fund house
* category - Text - Fund category
* plan - Text - Plan type
* return_1yr_pct - Float - 1-year return
* return_3yr_pct - Float - 3-year return
* return_5yr_pct - Float - 5-year return
* benchmark_3yr_pct - Float - Benchmark return
* alpha - Float - Alpha metric
* beta - Float - Beta metric
* sharpe_ratio - Float - Sharpe ratio
* sortino_ratio - Float - Sortino ratio
* std_dev_ann_pct - Float - Annualized standard deviation
* max_drawdown_pct - Float - Maximum drawdown
* aum_crore - Integer - Assets under management
* expense_ratio_pct - Float - Expense ratio
* morningstar_rating - Integer - Morningstar rating
* risk_grade - Text - Risk grade



## 08_investor_transactions

* investor_id - Text - Unique investor ID
* transaction_date - Date - Transaction date
* amfi_code - Integer - AMFI scheme code
* transaction_type - Text - SIP/Lumpsum/Redemption
* amount_inr - Integer - Transaction amount
* state - Text - Investor state
* city - Text - Investor city
* city_tier - Text - City tier
* age_group - Text - Investor age group
* gender - Text - Investor gender
* annual_income_lakh - Float - Annual income
* payment_mode - Text - Payment method
* kyc_status - Text - KYC verification status



## 09_portfolio_holdings

* amfi_code - Integer - AMFI scheme code
* stock_symbol - Text - Stock symbol
* stock_name - Text - Company name
* sector - Text - Sector name
* weight_pct - Float - Portfolio weight percentage
* market_value_cr - Float - Market value in crore
* current_price_inr - Float - Current stock price
* portfolio_date - Date - Portfolio reporting date



## 10_benchmark_indices

* date - Date - Trading date
* index_name - Text - Benchmark index name
* close_value - Float - Closing index value
