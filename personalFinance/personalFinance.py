from base_graph import FinanceGraphBase

class PersonalFinance(FinanceGraphBase):
    def __init__(self):
        super().__init__('personal_finance')
        self.graph.node('root', 'Personal Finance', style='filled', fillcolor='#f4d8b2')

    def add_budgeting(self):
        self.graph.node('B', 'Budgeting', style='filled', fillcolor='#cce5ff')
        self.graph.edge('root', 'B')

    def add_savings(self):
        self.graph.node('S', 'Savings', style='filled', fillcolor='#d4edda')
        self.graph.edge('root', 'S')