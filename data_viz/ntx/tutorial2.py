import networkx as nx
import matplotlib.pyplot as plt 

nodes=["a","b","c","d","e"]
edges=[("a","c"),("b","c"),("b","d"),("c","d"),("d","e")]
G=nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos={
    "a":(1.0,5.0),
    "b":(4.5,6.6),
    "c":(3.6,1.4),
    "d":(5.8,3.5),
    "e":(7.9,3.6)
}
nx.draw(G,pos=pos,with_labels=True,node_color="lightblue",edge_color="gray",node_size=3000,font_size=20,font_color="white",font_family="Times New Roman",font_weight="bold",width=5)
plt.margins(0.2)
plt.show()
