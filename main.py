class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_neighbors(self, u):
        return self.graph.get(u, [])

    def vertices(self):
        return list(self.graph.keys())

class SocialNetworkAnalyzer:
    def __init__(self, social_network):
        self.G = Graph()
        self.social_network = social_network

    def build_network(self):
        for person, connections in self.social_network.items():
            for connection in connections:
                self.G.add_edge(person, connection)

    def visualize_network(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        # Create empty graph
        G_visualize = nx.Graph()

        # Add nodes and edges to visualize graph
        for person, connections in self.social_network.items():
            for connection in connections:
                G_visualize.add_edge(person, connection)

        # Visualize graph
        nx.draw(G_visualize, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        plt.title('Social Network Graph')
        plt.show()

    def degree_centrality(self):
        print("Degree Centrality:")
        for person in self.G.vertices():
            centrality = len(self.G.get_neighbors(person))
            print(f"{person}: {centrality}")

    def clustering_coefficients(self):
        print("\nClustering Coefficients:")
        for person in self.G.vertices():
            neighbors = self.G.get_neighbors(person)
            if len(neighbors) < 2:
                print(f"{person}: 0.0")
            else:
                triangles = sum(1 for v in neighbors for w in neighbors if v in self.G.get_neighbors(w))
                clustering_coefficient = triangles / (len(neighbors) * (len(neighbors) - 1))
                print(f"{person}: {clustering_coefficient:.4f}")

    def community_detection(self):
        # Using a simple approach for community detection
        visited = set()
        communities = []
        for person in self.G.vertices():
            if person not in visited:
                community = self.bfs(person)
                communities.append(community)
                visited.update(community)
        print("\nCommunities:")
        for i, community in enumerate(communities):
            print(f"Community {i+1}: {community}")

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            person = queue.pop(0)
            visited.add(person)
            for neighbor in self.G.get_neighbors(person):
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    def shortest_path(self, source, target):
        visited = set()
        queue = [(source, [source])]
        while queue:
            (node, path) = queue.pop(0)
            if node not in visited:
                if node == target:
                    return path
                visited.add(node)
                for neighbor in self.G.get_neighbors(node):
                    queue.append((neighbor, path + [neighbor]))
        return []

    def interactive_analysis(self):
        while True:
            print("\nInteractive Analysis Menu:")
            print("1. Degree Centrality")
            print("2. Clustering Coefficients")
            print("3. Community Detection")
            print("4. Shortest Path")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.degree_centrality()
            elif choice == '2':
                self.clustering_coefficients()
            elif choice == '3':
                self.community_detection()
            elif choice == '4':
                source = input("Enter source person: ")
                target = input("Enter target person: ")
                shortest_path = self.shortest_path(source, target)
                if shortest_path:
                    print(f"\nShortest path between {source} and {target}: {shortest_path}")
                else:
                    print(f"\nNo path found between {source} and {target}")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Sample social network data
social_network = {
    'Alice': ['Bob', 'Charlie', 'David'],
    'Bob': ['Alice', 'David'],
    'Charlie': ['Alice', 'David'],
    'David': ['Alice', 'Bob', 'Charlie']
}

# Create social network analyzer object
analyzer = SocialNetworkAnalyzer(social_network)
analyzer.build_network()

# Visualize network
analyzer.visualize_network()

# Interactive analysis
analyzer.interactive_analysis()
