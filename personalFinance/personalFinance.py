from base_graph import FinanceGraphBase

class PersonalFinance(FinanceGraphBase):
    COLOR = '#FFF7CC'
    
    def __init__(self):
        super().__init__('personal_finance')
        self.graph.node('root', 'Personal Finance', style='filled', fillcolor=self.COLOR)

    def add_budgeting(self):
        self.graph.node('B', 'Budgeting', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'B')

    def add_savings(self):
        self.graph.node('S', 'Savings', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'S')
    
    def add_investing(self):
        self.graph.node('I', 'Investing', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'I')