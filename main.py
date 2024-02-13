import networkx as nx
import matplotlib.pyplot as plt

# Sample social network data
social_network = {
    'Alice': ['Bob', 'Charlie', 'David'],
    'Bob': ['Alice', 'David'],
    'Charlie': ['Alice', 'David'],
    'David': ['Alice', 'Bob', 'Charlie']
}

# Create graph
G = nx.Graph()

# Add nodes and edges
for person, connections in social_network.items():
    G.add_node(person)
    for connection in connections:
        G.add_edge(person, connection)

# Visualize graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
plt.title('Social Network Graph')
plt.show()

# Analyze network
print("Degree Centrality:")
for person, centrality in nx.degree_centrality(G).items():
    print(f"{person}: {centrality}")

print("\nClustering Coefficients:")
for person, clustering_coefficient in nx.clustering(G).items():
    print(f"{person}: {clustering_coefficient}")
