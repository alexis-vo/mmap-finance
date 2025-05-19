from personalFinance.personalFinance import PersonalFinance
from corporateFinance.corporateFinance import CorporateFinance
from publicFinance.publicFinance import PublicFinance
from merge import FinanceMergeDynamic

def build_subgraphs(view=False):
    pf = PersonalFinance()
    pf.add_budgeting(); pf.add_savings()
    pf.generate(view=view)

    cf = CorporateFinance()
    cf.add_accounting(); cf.add_risk_management()
    cf.generate(view=view)

    pubf = PublicFinance()
    pubf.add_taxation()
    pubf.generate(view=view)

def main(view=False, merge_global=True):
    build_subgraphs(view=view)

    if merge_global:
        merger = FinanceMergeDynamic()
        merger.merge()
        merger.generate(view=view)

if __name__ == '__main__':
    main(view=False, merge_global=True)