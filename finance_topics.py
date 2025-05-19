from base_graph import FinanceGraphBase

class FinanceTopics(FinanceGraphBase):
    def __init__(self):
        super().__init__('finance_topics')
        self._build_graph()

    def _build_graph(self):
        g = self.graph
        g.node('root', 'Finance Topics', shape='doublecircle', style='filled', fillcolor='#a8c8f0')

        g.node('P', 'Personal',  style='filled', fillcolor='#f4d8b2')
        g.node('C', 'Corporate', style='filled', fillcolor='#c2e0c6')
        g.node('U', 'Public',    style='filled', fillcolor='#f0d6d6')
        g.edges([('root', 'P'), ('root', 'C'), ('root', 'U')])