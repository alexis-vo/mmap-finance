from base_graph import FinanceGraphBase

class CorporateFinance(FinanceGraphBase):
    COLOR = '#DDE9FF'

    def __init__(self):
        super().__init__('corporate_finance')
        self.graph.node('root', 'Corporate Finance', style='filled', fillcolor=self.COLOR)

    def add_capital(self):
        self.graph.node('C', 'Capital', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'C')

    def add_risk(self):
        self.graph.node('R', 'Risk', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'R')

    def add_growth(self):
        self.graph.node('G', 'Growth', style='filled', fillcolor=self.COLOR)
        self.graph.edge('root', 'G')

    # --- new branch for risk ----
    def add_financial_instruments(self):
        self.graph.node('FI', 'Financial Instruments', style='filled', fillcolor=self.COLOR)
        self.graph.edge('R', 'FI')

    def add_derivatives(self):
        self.graph.node('D', 'Derivatives', style='filled', fillcolor=self.COLOR)
        self.graph.edge('FI', 'D')

    def add_options(self):
        self.graph.node('O', 'Options', style='filled', fillcolor=self.COLOR)
        self.graph.edge('D', 'O')

    def add_option_pricing_models(self):
        self.graph.node('OPM', 'Option Pricing Models', style='filled', fillcolor=self.COLOR)
        self.graph.edge('O', 'OPM')

    def add_crr_model(self):
        self.graph.node('CRR', 'Cox Ross Rubinstein Model', style='filled', fillcolor=self.COLOR)
        self.graph.edge('OPM', 'CRR')