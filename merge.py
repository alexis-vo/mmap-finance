import os
import pydot
from graphviz import Digraph

class FinanceMergeDynamic:
    def __init__(self, input_folder='generatedGraphs', output_folder='generatedGraphs'):
        self.input_folder  = input_folder
        self.output_folder = output_folder
        self.final         = Digraph(comment='Merged Finance Topics')
        self.final.attr(rankdir='TB')
        self.final.node('F', 'Finance', style='filled', fillcolor='#a0a0a0', fontcolor='white')

    def merge(self):
        dot_files = [f for f in os.listdir(self.input_folder) if f.endswith('.dot')]
        for dot_file in dot_files:
            filepath = os.path.join(self.input_folder, dot_file)
            prefix   = os.path.splitext(dot_file)[0]
            self._add_subgraph(filepath, prefix)

    def _add_subgraph(self, filepath, prefix):
        def _clean(attr):
            """Supprime guillemets et espaces autour d’un attribut."""
            if attr is None:
                return ''
            return attr.strip(' "\'')

        graphs = pydot.graph_from_dot_file(filepath)
        if not graphs:
            return
        g = graphs[0]

        # node copy
        for node in g.get_nodes():
            name   = node.get_name().strip('"')
            attrs  = node.get_attributes()

            new_id = f'{prefix}_{name}'
            self.final.node(
                new_id,
                label     = _clean(attrs.get('label', name)),
                style     = _clean(attrs.get('style', '')),
                fillcolor = _clean(attrs.get('fillcolor', ''))
            )
        
        # edge copy
        for edge in g.get_edges():
            src  = f"{prefix}_{edge.get_source().strip('\"')}"
            dst  = f"{prefix}_{edge.get_destination().strip('\"')}"
            self.final.edge(src, dst)

        root_node = g.get_nodes()[0].get_name().strip('"')
        self.final.edge('F', f'{prefix}_{root_node}')

    def generate(self, filename='merged_finance', view=False):
        path = os.path.join(self.output_folder, filename)
        self.final.render(path, view=view, format='pdf')