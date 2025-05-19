from graphviz import Digraph
from pathlib import Path

GENERATED_DIR = Path('generatedGraphs')
GENERATED_DIR.mkdir(exist_ok=True)

class FinanceGraphBase:
    """Base class for finance-related graphs."""

    def __init__(self, name, rankdir='TB'):
        self.name = name
        self.graph = Digraph(comment=name)
        self.graph.attr(rankdir=rankdir)

    def generate(self, view=False, fmt='pdf'):
        """Create <name>.<fmt> + <name>.dot in generatedGraphs/."""
        out = GENERATED_DIR / self.name

        self.graph.render(
            filename=str(out),
            format=fmt,
            view=view,
            cleanup=True
        )

        (GENERATED_DIR / f'{self.name}.dot').write_text(
            self.graph.source, encoding='utf-8'
        )