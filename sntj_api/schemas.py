from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal

class Symbol(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    symbol_id : str
    symbol_name : Optional[str] = None
    cik : Optional[str] = None
    isin : Optional[str] = None
    cusip : Optional[str] = None
    ein_employer_id : Optional[str] = None
    lei : Optional[str] = None
    series_id : Optional[str] = None
    item_type : Optional[str] = None
    sector : Optional[str] = None
    industry : Optional[str] = None
    sic_code : Optional[str] = None
    sic_name : Optional[str] = None



class BalanceSheet(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    symbol : str
    year : int
    name : Optional[str] = None
    accounts_payable_current : Optional[Decimal] = None
    accounts_receivable_current : Optional[Decimal] = None
    accumulated_oci_loss_net_of_tax : Optional[Decimal] = None
    assets : Optional[Decimal] = None
    assets_current : Optional[Decimal] = None
    assets_noncurrent : Optional[Decimal] = None
    cash_cash_equivalents_at_carrying_value : Optional[Decimal] = None
    commercial_paper : Optional[Decimal] = None
    commitments_contingencies : Optional[str] = None
    common_stock_shares_issued : Optional[Decimal] = None
    common_stock_shares_outstanding : Optional[Decimal] = None
    common_stocks_additional_paid_in_capital : Optional[Decimal] = None
    contract_customer_liability_current : Optional[Decimal] = None
    inventory : Optional[Decimal] = None
    liabilities : Optional[Decimal] = None
    liabilities_stockholders_equity : Optional[Decimal] = None
    liabilities_current : Optional[Decimal] = None
    liabilities_noncurrent : Optional[Decimal] = None
    long_term_debt_current : Optional[Decimal] = None
    long_term_debt_noncurrent : Optional[Decimal] = None
    marketable_securities_current : Optional[Decimal] = None
    marketable_securities_noncurrent : Optional[Decimal] = None
    nontrade_receivables_current : Optional[Decimal] = None
    other_assets_current : Optional[Decimal] = None
    other_assets_noncurrent : Optional[Decimal] = None
    other_liabilities_current : Optional[Decimal] = None
    other_liabilities_noncurrent : Optional[Decimal] = None
    property_plant_equipment : Optional[Decimal] = None
    retained_earnings_accumulated_deficit : Optional[Decimal] = None
    stockholders_equity : Optional[Decimal] = None
    accounts_payable_accrued_liabilities_current : Optional[Decimal] = None
    accrued_liabilities_current : Optional[Decimal] = None
    additional_paid_in_capital : Optional[Decimal] = None
    common_stock_value : Optional[Decimal] = None
    contract_customer_liability : Optional[Decimal] = None
    deferred_income_tax_assets : Optional[Decimal] = None
    deferred_revenue_current : Optional[Decimal] = None
    funds_held_for_clients : Optional[Decimal] = None
    goodwill : Optional[Decimal] = None
    intangible_assets_excluding_goodwill : Optional[Decimal] = None
    intangible_assets_goodwill : Optional[Decimal] = None
    operating_lease_liability_current : Optional[Decimal] = None
    operating_lease_liability_noncurrent : Optional[Decimal] = None
    operating_lease_right_of_use_asset : Optional[Decimal] = None
    prepaid_expense_other_assets_current : Optional[Decimal] = None
    short_term_investments : Optional[Decimal] = None
    accumulated_oci_available_sale_securities_net_of_tax : Optional[Decimal] = None
    accumulated_oci_pension_postretirement_net_of_tax : Optional[Decimal] = None
    accumulated_oci_foreign_currency_net_of_tax : Optional[Decimal] = None
    aoci_loss_cash_flow_hedge_cumulative_gain_loss_after_tax : Optional[Decimal] = None
    available_for_sale_securities_debt_securities_noncurrent : Optional[Decimal] = None
    deferred_income_tax_liabilities : Optional[Decimal] = None
    employee_related_liabilities_current : Optional[Decimal] = None
    investments : Optional[Decimal] = None
    litigation_reserve_current : Optional[Decimal] = None
    long_term_investments : Optional[Decimal] = None
    accrued_litigation_current : Optional[Decimal] = None
    client_incentives_assets_current : Optional[Decimal] = None
    client_incentives_assets_noncurrent : Optional[Decimal] = None
    client_incentives_liabilities_current : Optional[Decimal] = None
    customer_collateral_assets : Optional[Decimal] = None
    customer_collateral_liabilities : Optional[Decimal] = None
    restricted_cash_cash_equivalents_us_litigation_escrow : Optional[Decimal] = None
    right_to_recover_for_covered_losses : Optional[Decimal] = None
    settlement_payable : Optional[Decimal] = None
    settlement_receivable : Optional[Decimal] = None
    covered_loss_protection_interchange_fees : Optional[Decimal] = None
    accrued_liabilities_current_avg : Optional[Decimal] = None
    common_stock_value_outstanding_avg : Optional[Decimal] = None
    preferred_stock_value_outstanding_avg : Optional[Decimal] = None
    stockholders_equity_noncontrolling_interest_avg : Optional[Decimal] = None
    tsla_digital_assets_non_current : Optional[Decimal] = None
    tsla_accrued_other_current_liabilities : Optional[Decimal] = None
    tsla_long_term_debt_finance_leases_current : Optional[Decimal] = None
    tsla_long_term_debt_finance_leases_noncurrent : Optional[Decimal] = None
    contract_customer_liability_noncurrent : Optional[Decimal] = None
    redeemable_noncontrolling_interest_equity_carrying_amount : Optional[Decimal] = None
    preferred_stock_value : Optional[Decimal] = None
    additional_paid_in_capital_common_stock : Optional[Decimal] = None
    minority_interest : Optional[Decimal] = None
    deferred_costs_leasing_noncurrent_avg : Optional[Decimal] = None
    tsla_leased_assets_avg : Optional[Decimal] = None
    accounts_payable_other_accrued_liabilities_current : Optional[Decimal] = None
    available_for_sale_securities_debt_securities_current : Optional[Decimal] = None
    capitalized_contract_cost_current : Optional[Decimal] = None
    capitalized_contract_cost_noncurrent : Optional[Decimal] = None
    convertible_debt_current : Optional[Decimal] = None
    other_long_term_investments : Optional[Decimal] = None
    net_ppe_finance_lease_assets : Optional[Decimal] = None
    treasury_stock_common_value : Optional[Decimal] = None