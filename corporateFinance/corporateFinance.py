from base_graph import FinanceGraphBase

class CorporateFinance(FinanceGraphBase):
    COLOR = '#DDE9FF'

    def __init__(self):
        super().__init__('corporate_finance')
        self.graph.node('root', 'Corporate Finance', style='filled', fillcolor=self.COLOR)

    def add_capital(self):
        self.graph.node('C', 'Capital', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'C')

    def add_risk(self):
        self.graph.node('R', 'Risk', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'R')

    def add_growth(self):
        self.graph.node('G', 'Growth', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'G')
