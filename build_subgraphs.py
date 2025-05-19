from personalFinance.personalFinance import PersonalFinance
from corporateFinance.corporateFinance import CorporateFinance
from publicFinance.publicFinance import PublicFinance
from finance_topics import FinanceTopics

def build_subgraphs(view: bool = False) -> None:
    # --- Finance Topics (global graph) ---------------------------------
    # ft = FinanceTopics()
    # ft.generate(output_folder='.', view=view)

    # --- Personal -------------------------------------------------------
    pf = PersonalFinance()
    pf.add_budgeting()
    pf.add_savings()
    pf.add_investing()
    pf.generate(view=view)

    # --- Corporate ------------------------------------------------------
    cf = CorporateFinance()
    cf.add_capital()
    cf.add_risk()
    cf.add_growth()
    cf.add_financial_instruments()
    cf.add_derivatives()
    cf.add_options()
    cf.add_option_pricing_models()
    cf.add_crr_model()
    cf.generate(view=view)

    # --- Public ---------------------------------------------------------
    pubf = PublicFinance()
    pubf.add_taxation()
    pubf.add_spending()
    pubf.add_policy()
    pubf.generate(view=view)