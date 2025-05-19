class Savings:
    def add_to_graph(self, graph, parent_node):
        graph.node('S', 'Savings', style='filled', fillcolor='#d4edda')
        graph.edge(parent_node, 'S')
        # Ajoute ici d’autres noeuds spécifiques aux savings si besoin