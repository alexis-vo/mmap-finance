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
        """Create <GENERATED_DIR>/<fmt>/<name>.(fmt|dot)."""
        subdir_fmt = GENERATED_DIR / fmt
        subdir_fmt.mkdir(parents=True, exist_ok=True)
        subdir_dot = GENERATED_DIR / 'dot'
        subdir_dot.mkdir(parents=True, exist_ok=True)

        outfile = subdir_fmt / self.name
        self.graph.render(
            filename=str(outfile),
            format=fmt,
            view=view,
            cleanup=True
        )

        dot_path = subdir_dot / f'{self.name}.dot'
        dot_path.write_text(self.graph.source, encoding='utf-8')