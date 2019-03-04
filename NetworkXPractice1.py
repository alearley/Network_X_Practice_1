import networkx as nx
G = nx.Graph()
G.add_edges_from ([(1, 2), (1, 3)]) #Will take negative numbers
G.add_node(4)
G.add_edge(1, 4)
G.add_nodes_from("test")  #won't add letters more than once
G.add_edge(3, 's')
G.remove_nodes_from("test")
print("G's nodes:", (G.nodes))
print("G's edges:", (G.edges))
print("Number of nodes in G:", G.number_of_nodes())
print("Number of edges in G:", G.number_of_edges())
print("G[1]'s neighbors:", list(G.adj[1]))  # or list(G.neighbors(1))
print("Number of edges incident to 1:", G.degree[1])  # the number of edges incident to 1
print("Number of edges incident to 3:", G.degree[3])
print("Degree of each node:", G.degree([1, 3]))