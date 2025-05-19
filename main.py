from personalFinance.personalFinance import PersonalFinance
from corporateFinance import CorporateFinance
from publicFinance import PublicFinance
from merge import FinanceMergeDynamic

def build_subgraphs(output_folder = 'generatedGraphs', view=False):
    
    # Personal
    personal = PersonalFinance()
    personal.add_budgeting()
    personal.add_savings()
    personal.generate(output_path=f'{output_folder}/personal_finance', view=view)

    # Corporate
    corporate = CorporateFinance()
    corporate.add_accounting()
    corporate.add_risk_management()
    corporate.generate(output_path=f'{output_folder}/corporate_finance', view=view)

    # Public
    public = PublicFinance()
    public.add_taxation()
    public.generate(output_path=f'{output_folder}/public_finance', view=view)

def main(view=False, merge_global=True):
    build_subgraphs(view=view)

    if merge_global:
        merger = FinanceMergeDynamic()
        merger.merge()
        merger.generate(view=view)

    

if __name__ == '__main__':
    main(view=False, merge_global=True)