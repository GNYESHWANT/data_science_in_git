import networkx as nx
import matplotlib.pyplot as plt 

nodes=[0,1,2,3,4]
edges=[(0,1),(0,2),(1,3),(2,3),(3,4)]
G=nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color="lightblue",edge_color="gray",node_size=3000,font_size=20)
plt.margins(0.2)
plt.show()
