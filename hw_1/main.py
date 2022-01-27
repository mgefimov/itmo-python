import ast
import inspect
from fib import fib
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.Graph()
    source = inspect.getsource(fib)
    ast_obj = ast.parse(source)

    print(ast.dump(ast_obj, indent=2))


    def build_graph(parent):
        for node in ast.iter_child_nodes(parent):
            if ast.unparse(parent) != ast.unparse(node) and len(ast.unparse(node)) > 0:
                G.add_edge(ast.unparse(parent), ast.unparse(node))
            build_graph(node)


    build_graph(ast_obj)
    plt.figure(figsize=(10, 6))
    nx.draw_circular(G, with_labels=True)
    plt.savefig('artifacts/fig.jpg')
