from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, BigInteger, Date, Boolean
from sqlalchemy.orm import relationship

from database import Base

class DimSymbol(Base):
    __tablename__ = "dim_symbol"

    symbol_id = Column(String, primary_key=True, index=True)
    symbol_name = Column(String)
    cik = Column(String)
    isin = Column(String)
    cusip = Column(String)
    ein_employer_id = Column(String)
    lei = Column(String)
    series_id = Column(String)
    item_type = Column(String)
    sector = Column(String)
    industry = Column(String)
    sic_code = Column(String)
    sic_name = Column(String)

    balance_sheets = relationship("BalanceSheet", back_populates="dim_symbol")
    ohlc_daily_data = relationship("FactOHLCDaily", back_populates="dim_symbol")
    cashflows = relationship("Cashflow", back_populates="dim_symbol")
    income_statements = relationship("IncomeStatement", back_populates="dim_symbol")
    operation_statements = relationship("StatementOPeration", back_populates="dim_symbol")

class BalanceSheet(Base):
    __tablename__ = "fact_balance_sheet"

    symbol = Column(String, ForeignKey("dim_symbol.symbol_id"), primary_key=True, index=True)
    year = Column(Integer, primary_key=True, index=True)
    accounts_payable_current = Column(Numeric)
    accounts_receivable_current = Column(Numeric)
    accumulated_oci_loss_net_of_tax = Column(Numeric)
    assets = Column(Numeric)
    assets_current = Column(Numeric)
    assets_noncurrent = Column(Numeric)
    cash_cash_equivalents_at_carrying_value = Column(Numeric)
    commercial_paper = Column(Numeric)
    commitments_contingencies = Column(String)
    common_stock_shares_issued = Column(Numeric)
    common_stock_shares_outstanding = Column(Numeric)
    common_stocks_additional_paid_in_capital = Column(Numeric)
    contract_customer_liability_current = Column(Numeric)
    inventory = Column(Numeric)
    liabilities = Column(Numeric)
    liabilities_stockholders_equity = Column(Numeric)
    liabilities_current = Column(Numeric)
    liabilities_noncurrent = Column(Numeric)
    long_term_debt_current = Column(Numeric)
    long_term_debt_noncurrent = Column(Numeric)
    marketable_securities_current = Column(Numeric)
    marketable_securities_noncurrent = Column(Numeric)
    nontrade_receivables_current = Column(Numeric)
    other_assets_current = Column(Numeric)
    other_assets_noncurrent = Column(Numeric)
    other_liabilities_current = Column(Numeric)
    other_liabilities_noncurrent = Column(Numeric)
    property_plant_equipment = Column(Numeric)
    retained_earnings_accumulated_deficit = Column(Numeric)
    stockholders_equity = Column(Numeric)
    accounts_payable_accrued_liabilities_current = Column(Numeric)
    accrued_liabilities_current = Column(Numeric)
    additional_paid_in_capital = Column(Numeric)
    common_stock_value = Column(Numeric)
    contract_customer_liability = Column(Numeric)
    deferred_income_tax_assets = Column(Numeric)
    deferred_revenue_current = Column(Numeric)
    funds_held_for_clients = Column(Numeric)
    goodwill = Column(Numeric)
    intangible_assets_excluding_goodwill = Column(Numeric)
    intangible_assets_goodwill = Column(Numeric)
    operating_lease_liability_current = Column(Numeric)
    operating_lease_liability_noncurrent = Column(Numeric)
    operating_lease_right_of_use_asset = Column(Numeric)
    prepaid_expense_other_assets_current = Column(Numeric)
    short_term_investments = Column(Numeric)
    accumulated_oci_available_sale_securities_net_of_tax = Column(Numeric)
    accumulated_oci_pension_postretirement_net_of_tax = Column(Numeric)
    accumulated_oci_foreign_currency_net_of_tax = Column(Numeric)
    aoci_loss_cash_flow_hedge_cumulative_gain_loss_after_tax = Column(Numeric)
    available_for_sale_securities_debt_securities_noncurrent = Column(Numeric)
    deferred_income_tax_liabilities = Column(Numeric)
    employee_related_liabilities_current = Column(Numeric)
    investments = Column(Numeric)
    litigation_reserve_current = Column(Numeric)
    long_term_investments = Column(Numeric)
    accrued_litigation_current = Column(Numeric)
    client_incentives_assets_current = Column(Numeric)
    client_incentives_assets_noncurrent = Column(Numeric)
    client_incentives_liabilities_current = Column(Numeric)
    customer_collateral_assets = Column(Numeric)
    customer_collateral_liabilities = Column(Numeric)
    restricted_cash_cash_equivalents_us_litigation_escrow = Column(Numeric)
    right_to_recover_for_covered_losses = Column(Numeric)
    settlement_payable = Column(Numeric)
    settlement_receivable = Column(Numeric)
    covered_loss_protection_interchange_fees = Column(Numeric)
    accrued_liabilities_current_avg = Column(Numeric)
    common_stock_value_outstanding_avg = Column(Numeric)
    preferred_stock_value_outstanding_avg = Column(Numeric)
    stockholders_equity_noncontrolling_interest_avg = Column(Numeric)
    tsla_digital_assets_non_current = Column(Numeric)
    tsla_accrued_other_current_liabilities = Column(Numeric)
    tsla_long_term_debt_finance_leases_current = Column(Numeric)
    tsla_long_term_debt_finance_leases_noncurrent = Column(Numeric)
    contract_customer_liability_noncurrent = Column(Numeric)
    redeemable_noncontrolling_interest_equity_carrying_amount = Column(Numeric)
    preferred_stock_value = Column(Numeric)
    additional_paid_in_capital_common_stock = Column(Numeric)
    minority_interest = Column(Numeric)
    deferred_costs_leasing_noncurrent_avg = Column(Numeric)
    tsla_leased_assets_avg = Column(Numeric)
    accounts_payable_other_accrued_liabilities_current = Column(Numeric)
    available_for_sale_securities_debt_securities_current = Column(Numeric)
    capitalized_contract_cost_current = Column(Numeric)
    capitalized_contract_cost_noncurrent = Column(Numeric)
    convertible_debt_current = Column(Numeric)
    other_long_term_investments = Column(Numeric)
    net_ppe_finance_lease_assets = Column(Numeric)
    treasury_stock_common_value = Column(Numeric)



    dim_symbol = relationship("DimSymbol", back_populates="balance_sheets")

class DimExchange(Base):
    __tablename__ = "dim_exchange"

    exchange_ticker_id = Column(String, primary_key=True, index=True)
    exchange_id = Column(String, nullable=True)
    exchange_name = Column(String, nullable=True)
    acronym = Column(String, nullable=True)
    country_code = Column(String, nullable=True)
    city = Column(String, nullable=True)
    market_category_code = Column(String, nullable=True)
    exchange_status = Column(String, nullable=True)

    ohlc_daily_data = relationship("OHLCDaily", back_populates="dim_exchange")


class DimTimestamp(Base):
    __tablename__ = "dim_timestamp"

    timestamp_ms = Column(BigInteger, primary_key=True, index=True)
    date = Column(Date, nullable=True)
    day_of_the_week = Column(String, nullable=True)
    month = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    quarter = Column(Integer, nullable=True)
    fiscal_year = Column(Integer, nullable=True)
    is_weekend = Column(Boolean, nullable=True)
    is_public_holiday = Column(Boolean, nullable=True)


    ohlc_daily_data = relationship("OHLCDaily", back_populates="dim_timestamp")

class OHLCDaily(Base):
    __tablename__ = "fact_ohlc_daily"

    symbol_id = Column(String, ForeignKey("dim_symbol.symbol_id"), primary_key=True, nullable=False)
    timestamp_ms = Column(BigInteger, ForeignKey("dim_timestamp.timestamp_ms"), primary_key=True, nullable=False)
    exchange_id = Column(String, ForeignKey("dim_exchange.exchange_ticker_id"), primary_key=True, nullable=False) # Assuming exchange_ticker_id is used
    

    _open = Column(Numeric, nullable=True)
    _high = Column(Numeric, nullable=True)
    _low = Column(Numeric, nullable=True)
    _close = Column(Numeric, nullable=True)
    volume = Column(BigInteger, nullable=True)
    adj_high = Column(Numeric, nullable=True)
    adj_close = Column(Numeric, nullable=True)
    adj_low = Column(Numeric, nullable=True)
    adj_open = Column(Numeric, nullable=True)
    adj_volume = Column(BigInteger, nullable=True)
    split_factor = Column(Numeric, nullable=True)
    dividend = Column(Numeric, nullable=True)
    ADJ_SMA_10 = Column(Numeric, nullable=True)
    ADJ_SMA_20 = Column(Numeric, nullable=True)
    ADJ_SMA_50 = Column(Numeric, nullable=True)
    ADJ_SMA_100 = Column(Numeric, nullable=True)
    ADJ_SMA_200 = Column(Numeric, nullable=True)
    ADJ_EMA_12 = Column(Numeric, nullable=True)
    ADJ_EMA_26 = Column(Numeric, nullable=True)
    ADJ_EMA_50 = Column(Numeric, nullable=True)
    ADJ_EMA_100 = Column(Numeric, nullable=True)
    ADJ_WMA_30 = Column(Numeric, nullable=True)
    ADJ_HMA_30 = Column(Numeric, nullable=True)
    ADJ_DEMA_30 = Column(Numeric, nullable=True)
    ADJ_TEMA_30 = Column(Numeric, nullable=True)
    ADJ_RSI_14 = Column(Numeric, nullable=True)
    ADJ_RSI_7 = Column(Numeric, nullable=True)
    ADJ_MACD = Column(Numeric, nullable=True)
    ADJ_MACD_signal = Column(Numeric, nullable=True)
    ADJ_MACD_hist = Column(Numeric, nullable=True)
    ADJ_Stoch_K = Column(Numeric, nullable=True)
    ADJ_Stoch_D = Column(Numeric, nullable=True)
    ADJ_ATR_14 = Column(Numeric, nullable=True)
    ADJ_ADX_14 = Column(Numeric, nullable=True)
    ADJ_CCI_14 = Column(Numeric, nullable=True)
    ADJ_WILLR_14 = Column(Numeric, nullable=True)
    ADJ_AD = Column(Numeric, nullable=True)
    ADJ_OBV = Column(Numeric, nullable=True)
    ADJ_SAR = Column(Numeric, nullable=True)
    ADJ_MOM_10 = Column(Numeric, nullable=True)
    ADJ_ROC_10 = Column(Numeric, nullable=True)
    ADJ_MFI_14 = Column(Numeric, nullable=True)
    ADJ_ULTOSC = Column(Numeric, nullable=True)
    ADJ_TRIX = Column(Numeric, nullable=True)
    ADJ_KC_upper = Column(Numeric, nullable=True)
    ADJ_KC_middle = Column(Numeric, nullable=True)
    ADJ_KC_adj_lower = Column(Numeric, nullable=True)
    ADJ_Aroon_Up = Column(Numeric, nullable=True)
    ADJ_Aroon_Down = Column(Numeric, nullable=True)
    ADJ_Donchian_Upper = Column(Numeric, nullable=True)
    ADJ_Donchian_Middle = Column(Numeric, nullable=True)
    ADJ_Donchian_adj_lower = Column(Numeric, nullable=True)
    ADJ_CMO_14 = Column(Numeric, nullable=True)
    ADJ_Stoch_RSI_K = Column(Numeric, nullable=True)
    ADJ_Stoch_RSI_D = Column(Numeric, nullable=True)
    ADJ_EFI_13 = Column(Numeric, nullable=True)
    ADJ_VWAP = Column(Numeric, nullable=True)
    ADJ_Ichimoku_Tenkan_Sen = Column(Numeric, nullable=True)
    ADJ_Ichimoku_Kijun_Sen = Column(Numeric, nullable=True)
    ADJ_Ichimoku_Senkou_Span_A = Column(Numeric, nullable=True)
    ADJ_Ichimoku_Senkou_Span_B = Column(Numeric, nullable=True)
    ADJ_Ichimoku_Chikou_Span = Column(Numeric, nullable=True)
    ADJ_Pivot_Point = Column(Numeric, nullable=True)
    ADJ_R1 = Column(Numeric, nullable=True)
    ADJ_S1 = Column(Numeric, nullable=True)
    ADJ_R2 = Column(Numeric, nullable=True)
    ADJ_S2 = Column(Numeric, nullable=True)
    ADJ_Vortex_Plus = Column(Numeric, nullable=True)
    ADJ_Vortex_Minus = Column(Numeric, nullable=True)
    SMA_10 = Column(Numeric, nullable=True)
    SMA_20 = Column(Numeric, nullable=True)
    SMA_50 = Column(Numeric, nullable=True)
    SMA_100 = Column(Numeric, nullable=True)
    SMA_200 = Column(Numeric, nullable=True)
    EMA_12 = Column(Numeric, nullable=True)
    EMA_26 = Column(Numeric, nullable=True)
    EMA_50 = Column(Numeric, nullable=True)
    EMA_100 = Column(Numeric, nullable=True)
    WMA_30 = Column(Numeric, nullable=True)
    HMA_30 = Column(Numeric, nullable=True)
    DEMA_30 = Column(Numeric, nullable=True)
    TEMA_30 = Column(Numeric, nullable=True)
    RSI_14 = Column(Numeric, nullable=True)
    RSI_7 = Column(Numeric, nullable=True)
    MACD = Column(Numeric, nullable=True)
    MACD_signal = Column(Numeric, nullable=True)
    MACD_hist = Column(Numeric, nullable=True)
    Stoch_K = Column(Numeric, nullable=True)
    Stoch_D = Column(Numeric, nullable=True)
    ATR_14 = Column(Numeric, nullable=True)
    ADX_14 = Column(Numeric, nullable=True)
    CCI_14 = Column(Numeric, nullable=True)
    WILLR_14 = Column(Numeric, nullable=True)
    AD = Column(Numeric, nullable=True)
    OBV = Column(Numeric, nullable=True)
    SAR = Column(Numeric, nullable=True)
    MOM_10 = Column(Numeric, nullable=True)
    ROC_10 = Column(Numeric, nullable=True)
    MFI_14 = Column(Numeric, nullable=True)
    ULTOSC = Column(Numeric, nullable=True)
    TRIX = Column(Numeric, nullable=True)
    KC_upper = Column(Numeric, nullable=True)
    KC_middle = Column(Numeric, nullable=True)
    KC_lower = Column(Numeric, nullable=True)
    Aroon_Up = Column(Numeric, nullable=True)
    Aroon_Down = Column(Numeric, nullable=True)
    Donchian_Upper = Column(Numeric, nullable=True)
    Donchian_Middle = Column(Numeric, nullable=True)
    Donchian_Lower = Column(Numeric, nullable=True)
    CMO_14 = Column(Numeric, nullable=True)
    Stoch_RSI_K = Column(Numeric, nullable=True)
    Stoch_RSI_D = Column(Numeric, nullable=True)
    EFI_13 = Column(Numeric, nullable=True)
    VWAP = Column(Numeric, nullable=True)
    Ichimoku_Tenkan_Sen = Column(Numeric, nullable=True)
    Ichimoku_Kijun_Sen = Column(Numeric, nullable=True)
    Ichimoku_Senkou_Span_A = Column(Numeric, nullable=True)
    Ichimoku_Senkou_Span_B = Column(Numeric, nullable=True)
    Ichimoku_Chikou_Span = Column(Numeric, nullable=True)
    Pivot_Point = Column(Numeric, nullable=True)
    R1 = Column(Numeric, nullable=True)
    S1 = Column(Numeric, nullable=True)
    R2 = Column(Numeric, nullable=True)
    S2 = Column(Numeric, nullable=True)
    Vortex_Plus = Column(Numeric, nullable=True)
    Vortex_Minus = Column(Numeric, nullable=True)


    dim_symbol = relationship("DimSymbol", back_populates="ohlc_daily_data")
    dim_timestamp = relationship("DimTimestamp", back_populates="ohlc_daily_data")
    dim_exchange = relationship("DimExchange", back_populates="ohlc_daily_data")


class CashFlow(Base):
    __tablename__ = "fact_cash_flow"
    symbol = Column(String, ForeignKey("dim_symbol.symbol_id"), nullable=False)
    year = Column(Integer, primary_key=True, index=True)

    cash_equivalents_restricted_cash = Column(Numeric, nullable=True)
    cash_equivalents_restricted_cash_change_exchange = Column(Numeric, nullable=True)
    deferred_income_tax_expense_benefit = Column(Numeric, nullable=True)
    depreciation_depletion___amortization = Column(Numeric, nullable=True)
    income_taxes_paid__ = Column(Numeric, nullable=True)
    increase_decrease_in_accounts_payable = Column(Numeric, nullable=True)
    increase_decrease_in_accounts_receivable = Column(Numeric, nullable=True)
    change_contract_customer_liability = Column(Numeric, nullable=True)
    increase_decrease_in_inventories = Column(Numeric, nullable=True)
    increase_decrease_in_other_operating_assets = Column(Numeric, nullable=True)
    change_other_operating_liabilities = Column(Numeric, nullable=True)
    increase_decrease_in_other_receivables = Column(Numeric, nullable=True)
    interest_paid__ = Column(Numeric, nullable=True)
    __cash_provided_by_used_in_financing_activities = Column(Numeric, nullable=True)
    __cash_provided_by_used_in_investing_activities = Column(Numeric, nullable=True)
    __cash_provided_by_used_in_operating_activities = Column(Numeric, nullable=True)
    __income_loss = Column(Numeric, nullable=True)
    other_noncash_income_expense = Column(Numeric, nullable=True)
    payments_for_proceeds_from_other_investing_activities = Column(Numeric, nullable=True)
    payments_for_repurchase_of_common_stock = Column(Numeric, nullable=True)
    payments_of_dividends = Column(Numeric, nullable=True)
    payments_tax_withholding_share_compensation = Column(Numeric, nullable=True)
    payments_to_acquire_available_for_sale_securities_debt = Column(Numeric, nullable=True)
    payments_acquire_businesses_net_cash = Column(Numeric, nullable=True)
    payments_to_acquire_other_investments = Column(Numeric, nullable=True)
    payments_to_acquire_property_plant___equipment = Column(Numeric, nullable=True)
    proceeds_from_issuance_of_common_stock = Column(Numeric, nullable=True)
    proceeds_from_issuance_of_long_term_debt = Column(Numeric, nullable=True)
    proceeds_maturities_prepayments_available_sale = Column(Numeric, nullable=True)
    proceeds_other_financing_activities = Column(Numeric, nullable=True)
    proceeds_from_repayments_of_commercial_paper = Column(Numeric, nullable=True)
    proceeds_sale_maturity_other_investments = Column(Numeric, nullable=True)
    proceeds_from_sale_of_available_for_sale_securities_debt = Column(Numeric, nullable=True)
    repayments_of_long_term_debt = Column(Numeric, nullable=True)
    share_based_compensation = Column(Numeric, nullable=True)
    change_funds_payable_customers = Column(Numeric, nullable=True)
    change_operating_lease_liabilities = Column(Numeric, nullable=True)
    change_operating_lease_right_use_assets = Column(Numeric, nullable=True)
    investment_impairment_charges = Column(Numeric, nullable=True)
    payment_capped_calls_convertible_notes = Column(Numeric, nullable=True)
    proceeds_longterm_debt_warrants = Column(Numeric, nullable=True)
    asset_impairment_charges = Column(Numeric, nullable=True)
    deferred_income_taxes___tax_credits = Column(Numeric, nullable=True)
    exchange_rate_effect_cash_equivalents_restricted_cash = Column(Numeric, nullable=True)
    fair_value_adjustment_of_warrants = Column(Numeric, nullable=True)
    foreign_currency_transaction_gain_loss = Column(Numeric, nullable=True)
    gain_loss_on_sale_of_investments = Column(Numeric, nullable=True)
    gains_losses_on_extinguishment_of_debt = Column(Numeric, nullable=True)
    income_taxes_paid = Column(Numeric, nullable=True)
    increase_decrease_in_accrued_liabilities = Column(Numeric, nullable=True)
    increase_decrease_in_deferred_revenue = Column(Numeric, nullable=True)
    change_prepaid_deferred_expense_assets = Column(Numeric, nullable=True)
    other_depreciation___amortization = Column(Numeric, nullable=True)
    other_operating_activities_cash_flow_statement = Column(Numeric, nullable=True)
    payments_of_debt_extinguishment_costs = Column(Numeric, nullable=True)
    payments_to_acquire_short_term_investments = Column(Numeric, nullable=True)
    proceeds_from_convertible_debt = Column(Numeric, nullable=True)
    proceeds_from_issuance_initial_public_offering = Column(Numeric, nullable=True)
    proceeds_issuance_shares_incentive_compensation = Column(Numeric, nullable=True)
    proceeds_issuance_shares_incentive_compensation_options = Column(Numeric, nullable=True)
    proceeds_maturities_prepayments_shortterm_investments = Column(Numeric, nullable=True)
    proceeds_sale_maturity_marketable_securities = Column(Numeric, nullable=True)
    proceeds_from_sale_of_short_term_investments = Column(Numeric, nullable=True)
    proceeds_from_stock_options_exercised = Column(Numeric, nullable=True)
    provision_for_doubtful_accounts = Column(Numeric, nullable=True)
    business_combination_equity_awards = Column(Numeric, nullable=True)
    deferred_tax_intra_entity_intangible = Column(Numeric, nullable=True)
    fair_value_adjustment_performance_obligations = Column(Numeric, nullable=True)
    change_capitalized_contract_costs = Column(Numeric, nullable=True)
    noncash_acquisition_consideration = Column(Numeric, nullable=True)
    repayments_convertible_debt_capped_calls = Column(Numeric, nullable=True)
    capitalized_contract_cost_amortization = Column(Numeric, nullable=True)
    depreciation___amortization = Column(Numeric, nullable=True)
    finance_lease_principal_payments = Column(Numeric, nullable=True)
    gain_loss_on_investments = Column(Numeric, nullable=True)
    change_accounts_payable_accrued_liabilities = Column(Numeric, nullable=True)
    increase_decrease_in_operating_lease_liability = Column(Numeric, nullable=True)
    payments_to_acquire_longterm_investments = Column(Numeric, nullable=True)
    proceeds_from_issuance_of_medium_term_notes = Column(Numeric, nullable=True)
    proceeds_from_sale_of_longterm_investments = Column(Numeric, nullable=True)
    proceeds_from_stock_plans = Column(Numeric, nullable=True)
    repayments_of_long_term_lines_of_credit = Column(Numeric, nullable=True)
    profit_loss = Column(Numeric, nullable=True)
    tsla__depreciation_amortization___impairment = Column(Numeric, nullable=True)
    inventory_write_down = Column(Numeric, nullable=True)
    foreign_currency_transaction_gain_loss_unrealized = Column(Numeric, nullable=True)
    tsla__noncash_interest_income_expense___other_operating_activities = Column(Numeric, nullable=True)
    tsla__gain_loss_on_digital_assets = Column(Numeric, nullable=True)
    tsla__increase_decrease_in_operating_lease_vehicles = Column(Numeric, nullable=True)
    tsla__payments_for_solar_energy_systems___of_sales = Column(Numeric, nullable=True)
    tsla__proceeds_from_sales_of_digital_assets = Column(Numeric, nullable=True)
    tsla__payments_to_acquire_other_indefinite_lived_intangible_assets = Column(Numeric, nullable=True)
    payments_to_acquire_investments = Column(Numeric, nullable=True)
    proceeds_from_sale_maturity___collections_of_investments = Column(Numeric, nullable=True)
    tsla__government_grant_receipt = Column(Numeric, nullable=True)
    proceeds_from_issuance_of_debt = Column(Numeric, nullable=True)
    repayments_of_convertible_debt = Column(Numeric, nullable=True)
    payments_of_debt_issuance_costs = Column(Numeric, nullable=True)
    payments_to_minority_shareholders = Column(Numeric, nullable=True)
    tsla__payments_for_buy_outs_of_noncontrolling_interests_in_subsidiaries = Column(Numeric, nullable=True)
    effect_of_exchange_rate_on_cash = Column(Numeric, nullable=True)
    cash_cash_equivalents = Column(Numeric, nullable=True)
    noncash_or_part_noncash_acquisition_value_of_assets_acquired1 = Column(Numeric, nullable=True)
    capital_expenditures_incurred_but_not_yet_paid = Column(Numeric, nullable=True)
    exchange_rate_effect_cash_equivalents = Column(Numeric, nullable=True)
    change_accrued_liabilities_operating_liabilities = Column(Numeric, nullable=True)
    payment_contingent_consideration_liability_financing = Column(Numeric, nullable=True)
    payments_derivative_instrument_financing = Column(Numeric, nullable=True)
    payments_proceeds_derivative_instrument_investing = Column(Numeric, nullable=True)
    payments_to_acquire_productive_assets = Column(Numeric, nullable=True)
    proceeds_sale_maturity_available_sale = Column(Numeric, nullable=True)
    amortization_client_incentives = Column(Numeric, nullable=True)
    amortization_volume_support_incentives = Column(Numeric, nullable=True)
    equity_investments_fair_value_income = Column(Numeric, nullable=True)
    change_accrued_litigation = Column(Numeric, nullable=True)
    change_client_incentives = Column(Numeric, nullable=True)
    change_settlement_payable = Column(Numeric, nullable=True)
    change_settlement_receivable = Column(Numeric, nullable=True)
    change_volume_support_incentives = Column(Numeric, nullable=True)
    noncash_contribution_expense = Column(Numeric, nullable=True)
    proceeds_sharebased_tax_compensation = Column(Numeric, nullable=True)
    territory_covered_losses_post_acquisition = Column(Numeric, nullable=True)

    dim_symbol = relationship("DimSymbol", back_populates="cashflows")

class IncomeStatement(Base):
    symbol = Column(String, ForeignKey("dim_symbol.symbol_id"), nullable=False)
    year = Column(Integer, primary_key=True, index=True)

    oci_derivative_reclassification_after_tax = Column(Numeric, nullable=True)
    oci_derivative_after_reclassification_tax = Column(Numeric, nullable=True)
    oci_derivative_before_reclassification_after_tax = Column(Numeric, nullable=True)
    comprehensive_income___of_tax = Column(Numeric, nullable=True)
    __income_loss = Column(Numeric, nullable=True)
    oci_available_sale_securities_net_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge_reclassification_after_tax = Column(Numeric, nullable=True)
    oci_derivatives_hedges_net_tax = Column(Numeric, nullable=True)
    oci_foreign_currency_translation_net_tax = Column(Numeric, nullable=True)
    oci_net_tax_parent = Column(Numeric, nullable=True)
    oci_reclassification_sale_securities_net_tax = Column(Numeric, nullable=True)
    oci_reclassification_derivatives_net_tax = Column(Numeric, nullable=True)
    oci_unrealized_derivatives_net_tax = Column(Numeric, nullable=True)
    oci_unrealized_securities_net_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge_after_reclassification_tax_parent = Column(Numeric, nullable=True)
    oci_foreign_currency_translation_net_tax_parent = Column(Numeric, nullable=True)
    oci_foreign_currency_translation_before_tax_parent = Column(Numeric, nullable=True)
    oci_before_tax_parent = Column(Numeric, nullable=True)
    oci_tax_parent = Column(Numeric, nullable=True)
    oci_unrealized_securities_before_tax = Column(Numeric, nullable=True)
    profit_loss = Column(Numeric, nullable=True)
    unrealized_gain_loss_on_investments = Column(Numeric, nullable=True)
    tsla____loss_realized___included_in___income = Column(Numeric, nullable=True)
    comprehensive_income_net_tax_noncontrolling = Column(Numeric, nullable=True)
    comprehensive_income___of_tax_attributable_to_noncontrolling_interest = Column(Numeric, nullable=True)
    oci_pension_amortization_prior_service_before_tax = Column(Numeric, nullable=True)
    oci_pension_amortization_prior_service_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge_reclassification_before_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge_reclassification_tax = Column(Numeric, nullable=True)
    oci_foreign_currency_translation_before_tax = Column(Numeric, nullable=True)
    oci_foreign_currency_translation_tax = Column(Numeric, nullable=True)
    other_comprehensive_income_loss___of_tax = Column(Numeric, nullable=True)
    oci_reclassification_sale_securities_before_tax = Column(Numeric, nullable=True)
    oci_reclassification_sale_securities_tax = Column(Numeric, nullable=True)
    oci_unrealized_securities_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge = Column(Numeric, nullable=True)
    oci_cashflow_hedge_tax = Column(Numeric, nullable=True)
    oci_cashflow_hedge_before_reclassification_tax_avg = Column(Numeric, nullable=True)
    oci_pension_postretirement_before_adjustments_tax_avg = Column(Numeric, nullable=True)
    oci_cashflow_hedge_investment_before_reclassification_tax_avg = Column(Numeric, nullable=True)

    dim_symbol = relationship("DimSymbol", back_populates="income_statements")


class StatementOperation(Base):
    __tablename__ = "fact_statement_operation"

    symbol = Column(String, ForeignKey("dim_symbol.symbol_id"), nullable=False)
    year = Column(Integer, primary_key=True, index=True)

    earnings_per_share_basic = Column(Numeric, nullable=True)
    earnings_per_share_diluted = Column(Numeric, nullable=True)
    gross_profit = Column(Numeric, nullable=True)
    income_continuing_operations_before_tax = Column(Numeric, nullable=True)
    income_tax_expense_benefit = Column(Numeric, nullable=True)
    __income_loss = Column(Numeric, nullable=True)
    nonoperating_income_expense = Column(Numeric, nullable=True)
    operating_expenses = Column(Numeric, nullable=True)
    operating_income_loss = Column(Numeric, nullable=True)
    research___development_expense = Column(Numeric, nullable=True)
    selling_general___administrative_expense = Column(Numeric, nullable=True)
    weighted_average_diluted_shares = Column(Numeric, nullable=True)
    weighted_average_basic_shares = Column(Numeric, nullable=True)
    cost_of_goods___services_sold_avg = Column(Numeric, nullable=True)
    revenue_contract_customer_excluding_tax_avg = Column(Numeric, nullable=True)
    operations_support_expense = Column(Numeric, nullable=True)
    cost_of_revenue = Column(Numeric, nullable=True)
    costs___expenses = Column(Numeric, nullable=True)
    general___administrative_expense = Column(Numeric, nullable=True)
    income_continuing_operations_basic_share = Column(Numeric, nullable=True)
    income_continuing_operations_diluted_share = Column(Numeric, nullable=True)
    interest_income_expense_nonoperating__ = Column(Numeric, nullable=True)
    investment_income_nonoperating = Column(Numeric, nullable=True)
    other_nonoperating_income_expense = Column(Numeric, nullable=True)
    restructuring_charges = Column(Numeric, nullable=True)
    revenue_contract_customer_excluding_tax = Column(Numeric, nullable=True)
    selling___marketing_expense = Column(Numeric, nullable=True)
    fair_value_adjustment_performance_obligations = Column(Numeric, nullable=True)
    gain_loss_on_investments = Column(Numeric, nullable=True)
    income_continuing_operations_before_tax_equity_investments = Column(Numeric, nullable=True)
    other_nonoperating_expense = Column(Numeric, nullable=True)
    tsla__restructuring___other_expenses = Column(Numeric, nullable=True)
    investment_income_interest = Column(Numeric, nullable=True)
    interest_expense_nonoperating = Column(Numeric, nullable=True)
    profit_loss = Column(Numeric, nullable=True)
    __income_loss_attributable_to_noncontrolling_interest = Column(Numeric, nullable=True)
    cost_of_revenue_avg = Column(Numeric, nullable=True)
    communications___information_technology = Column(Numeric, nullable=True)
    depreciation___amortization = Column(Numeric, nullable=True)
    interest_income_expense__ = Column(Numeric, nullable=True)
    labor___related_expense = Column(Numeric, nullable=True)
    loss_contingency_loss_in_period = Column(Numeric, nullable=True)
    marketing___advertising_expense = Column(Numeric, nullable=True)
    professional_fees = Column(Numeric, nullable=True)
    revenues = Column(Numeric, nullable=True)
    earnings_per_share_basic_avg = Column(Numeric, nullable=True)
    earnings_per_share_diluted_avg = Column(Numeric, nullable=True)
    weighted_average_diluted_shares_avg = Column(Numeric, nullable=True)
    weighted_average_basic_shares_avg = Column(Numeric, nullable=True)

    dim_symbol = relationship("DimSymbol", back_populates="operation_statements")