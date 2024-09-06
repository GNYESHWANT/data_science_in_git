import networkx as nx
import matplotlib.pyplot as plt 
g=nx.Graph()
nodes=[1,2,3,4,5]
edges=[(1,2),(2,3),(2,4),(3,4),(4,5)]
g.add_nodes_from(nodes)
g.add_edges_from(edges)
pos=nx.spring_layout(g)
nx.draw(g,pos,with_labels=True,node_color="lightblue",edge_color="gray",node_size=3000,font_size=20)
plt.show()