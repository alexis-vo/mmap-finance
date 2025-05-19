from graphviz import Digraph

class PublicFinance:
    def __init__(self):
        self.graph = Digraph(comment='Public Finance')
        self.graph.node('PU', 'Public Finance', style='filled', fillcolor='#f0d6d6')

    def add_taxation(self):
        self.graph.node('T', 'Taxation')
        self.graph.edge('PU', 'T')

    def generate(self, output_path='public_finance', view=False):
        self.graph.render(output_path, view=view)

        dot_path = f'{output_path}.dot'
        with open(dot_path, 'w', encoding='utf-8') as f:
            f.write(self.graph.source)