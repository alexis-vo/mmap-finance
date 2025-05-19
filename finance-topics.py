from graphviz import Digraph

def finance_topics():
    """
    This function creates a directed graph using Graphviz to represent various finance topics.
    The graph includes nodes for Personal, Corporate, and Public finance, with subtopics for each.
    """
    # Create a new directed graph
    dot = Digraph(comment='Finance Topics')

    # Set graph attributes
    dot.node('A', 'Finance Topics', shape='doublecircle', style='filled', fillcolor='#a8c8f0')
    dot.node('B', 'Personal', style='filled', fillcolor='#f4d8b2')
    dot.node('C', 'Corporate', style='filled', fillcolor='#c2e0c6')
    dot.node('D', 'Public', style='filled', fillcolor='#f0d6d6')

    dot.edges(['AB', 'AC', 'AD'])
    dot.edge('B', 'Budgeting')
    dot.edge('B', 'Savings')
    dot.edge('B', 'Investing')
    dot.edge('C', 'Capital')
    dot.edge('C', 'Risk')
    dot.edge('C', 'Growth')
    dot.edge('D', 'Taxation')
    dot.edge('D', 'Spending')
    dot.edge('D', 'Policy')

dot.render('finance_topics', view=True)