from graphviz import Digraph

dot = Digraph(comment='Finance Topics')

# Couleurs sobres et pâles
dot.node('A', 'Finance Topics', shape='doublecircle', style='filled', fillcolor='#a8c8f0')  # bleu pastel
dot.node('B', 'Personal', style='filled', fillcolor='#f4d8b2')  # beige clair pastel
dot.node('C', 'Corporate', style='filled', fillcolor='#c2e0c6')  # vert pastel très clair
dot.node('D', 'Public', style='filled', fillcolor='#f0d6d6')  # rose pastel très clair

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

dot.render('finance_topics2', view=True)