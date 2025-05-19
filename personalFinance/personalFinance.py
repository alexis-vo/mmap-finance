from graphviz import Digraph
from personalFinance.budgeting import Budgeting
from personalFinance.savings import Savings

class PersonalFinance:
    def __init__(self):
        self.graph = Digraph(comment='Personal Finance')
        self.graph.node('P', 'Personal Finance', style='filled', fillcolor='#f4d8b2')

    def add_budgeting(self):
        Budgeting().add_to_graph(self.graph, 'P')

    def add_savings(self):
        Savings().add_to_graph(self.graph, 'P')

    def generate(self, output_path='personal_finance', view=False):
        self.graph.render(output_path, view=view)

        dot_path = f'{output_path}.dot'
        with open(dot_path, 'w', encoding='utf-8') as f:
            f.write(self.graph.source)