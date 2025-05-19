from base_graph import FinanceGraphBase

class CorporateFinance(FinanceGraphBase):
    def __init__(self):
        super().__init__('corporate_finance')
        self.graph.node('root', 'Corporate Finance', style='filled', fillcolor='#c2e0c6')

    def add_accounting(self):
        self.graph.node('A', 'Accounting')
        self.graph.edge('root', 'A')

    def add_risk_management(self):
        self.graph.node('R', 'Risk Management')
        self.graph.edge('root', 'R')
