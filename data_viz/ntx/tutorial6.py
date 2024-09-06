#maximum flow problem
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.flow import shortest_augmenting_path
g=nx.DiGraph()
g.add_nodes_from(["S","A","B","C","T"])
g.add_edges_from([
    ("S","A",{"capacity":12})
    ("S","B",{"capacity":8})
    ("S","C",{"capacity":5})
    ("A","B",{"capacity":10})
    ("A","C",{"capacity":9})
    ("B","T",{"capacity":5})
    ("C","B",{"capacity":7})
    ("C","T",{"capacity":16})
])
flow_value,flow_dict=nx.maximum_flow(g,"S","T",folw_func=shortest_augmenting_path)
print(flow_value)
print("=====================================")
print(flow_dict)
