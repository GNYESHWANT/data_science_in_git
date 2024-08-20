#altribute graph
import matplotlib.pyplot as plt 
import networkx as nx
G=nx.Graph()
G.graph["name"]="my Graph"
G.add_node("a",age=19,gender="F")
G.add_node("b",age=18,gender="M")
G.add_node("c",age=22,gender="M")
G.add_node("d",age=21,gender="M")
G.add_node("e",age=20,gender="F")
G.add_edge("a","c",weight=1)
G.add_edge("b","c",weight=0.5)
G.add_edge("b","d",weight=0.6)
G.add_edge("c","d",weight=0.8)
G.add_edge("d","e",weight=2)
pos={
    "a":(1.0,5.0),
    "b":(4.5,6.6),
    "c":(3.6,1.4),
    "d":(5.8,3.5),
    "e":(7.9,3.6)
}
pos_nod_attribute={
    "a":(-0.2,5.0),
    "b":(4.5,7.5),
    "c":(2.4,1.4),
    "d":(5.8,2.5),
    "e":(9.1,3.6)
}
for n,d in G.nodes(data=True):
    print(n)
    print(d)
    print("==========================================")
node_labels={n:(d["age"],d["gender"]) for n,d in G.nodes(data=True)}
edge_labels={(u,v):d["weight"] for u,v,d in G.edges(data=True)}
nx.draw(G,pos=pos,with_labels=True,node_color="lightblue",edge_color="gray",node_size=3000,font_size=20,font_color="white",font_family="Times New Roman",font_weight="bold",width=5)
nx.draw_networkx_labels(G,pos=pos_nod_attribute,labels=node_labels,font_color="black",font_family="Times New Roman",font_weight="bold")
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels,font_color="black",font_family="Times New Roman",font_weight="bold")
plt.margins(0.2)
plt.show()