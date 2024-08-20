import networkx as nx
import matplotlib.pyplot as plt 

nodes=[0,1,2,3,4]
edges=[(0,1),(0,2),(1,3),(2,3),(3,4)]
G=nx.Graph()
G.graph["name"]="My graph"
G.add_nodes_from(nodes)
G.add_edges_from(edges)
print(G.number_of_nodes())
print(G.number_of_edges())
print(f"#Nodes:{G.number_of_nodes()}")
print(f"#Edge:{G.number_of_edge()}")
for node in G.nodes:
    print(f"Degree({node})={G.degree(node)}")
    neighbour_list=[n for n in G.neighbors(node)]
    print(f"Neighbour({node})={neighbour_list}")
for edge in G.edges(data=True):
    print(edge)
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color="lightblue",edge_color="gray",node_size=3000,font_size=20)
plt.margins(0.2)
plt.show()