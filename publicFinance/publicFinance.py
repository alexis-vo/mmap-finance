from base_graph import FinanceGraphBase

class PublicFinance(FinanceGraphBase):
    def __init__(self):
        super().__init__('public_finance')
        self.graph.node('root', 'Public Finance', style='filled', fillcolor='#f0d6d6')

    def add_taxation(self):
        self.graph.node('T', 'Taxation')
        self.graph.edge('root', 'T')