class Budgeting:
    def add_to_graph(self, graph, parent_node):
        graph.node('B', 'Budgeting', style='filled', fillcolor='#cce5ff')
        graph.edge(parent_node, 'B')