from build_subgraphs import build_subgraphs
from merge import FinanceMergeDynamic

def main(view: bool = False, merge_global: bool = True) -> None:
    build_subgraphs(view=view)

    if merge_global:
        merger = FinanceMergeDynamic()
        merger.merge()
        merger.generate(view=view)

if __name__ == '__main__':
    main(view=False, merge_global=True)