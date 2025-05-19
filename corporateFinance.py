from graphviz import Digraph

class CorporateFinance:
    def __init__(self):
        self.graph = Digraph(comment='Corporate Finance')
        self.graph.node('C', 'Corporate Finance', style='filled', fillcolor='#c2e0c6')

    def add_accounting(self):
        self.graph.node('A', 'Accounting')
        self.graph.edge('C', 'A')

    def add_risk_management(self):
        self.graph.node('R', 'Risk Management')
        self.graph.edge('C', 'R')

    def generate(self, output_path='corporate_finance', view=False):
        self.graph.render(output_path, view=view)

        dot_path = f'{output_path}.dot'
        with open(dot_path, 'w', encoding='utf-8') as f:
            f.write(self.graph.source)