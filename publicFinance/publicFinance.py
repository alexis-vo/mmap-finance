from base_graph import FinanceGraphBase

class PublicFinance(FinanceGraphBase):
    COLOR = '#E8F7E8'

    def __init__(self):
        super().__init__('public_finance')
        self.graph.node('root', 'Public Finance', style='filled', fillcolor=self.COLOR)

    def add_taxation(self):
        self.graph.node('T', 'Taxation', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'T')

    def add_spending(self):
        self.graph.node('S', 'Spending', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'S')
    
    def add_policy(self):
        self.graph.node('P', 'Policy', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'P')