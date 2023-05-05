import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
## G = nx.MultiDiGraph()
## G = nx. Graph()
nodes=["0", "1", "2", "3"]
G.add_nodes_from(nodes)
G.add_edge("0","1")
G.add_edge("1","2")
G.add_edge("2","0")
G.add_edge("2","3")
G.add_edge("3","1")
print(G.nodes())
print(G.edges())
nx.draw(G, with_labels = True)
plt.savefig("simple_path.png") # zapis do pliku png
plt.show() # wyświetlenie