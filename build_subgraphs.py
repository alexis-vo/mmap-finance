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
    pf.generate(view=view)

    # --- Corporate ------------------------------------------------------
    cf = CorporateFinance()
    cf.add_accounting()
    cf.add_risk_management()
    cf.generate(view=view)

    # --- Public ---------------------------------------------------------
    pubf = PublicFinance()
    pubf.add_taxation()
    pubf.generate(view=view)