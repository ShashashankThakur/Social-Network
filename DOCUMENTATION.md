# Social Network Analysis Tool Documentation

This document provides an overview of the social network analysis tool implemented in Python. It includes information on the project structure, classes and methods, usage instructions, and sample social network data.

## Project Structure

The project consists of the following files:

- `main.py`: Main Python script implementing the social network analysis tool.
- `README.md`: README file providing information about the project, installation instructions, usage, and license details.
- `documentation.md`: Documentation file providing detailed information about the project structure, classes and methods, usage instructions, and sample social network data.
- `requirements.txt`: File listing dependencies required to run the project.

## Classes and Methods

### Graph Class

The `Graph` class represents a simple graph data structure.

#### Methods:

- `__init__()`: Initializes the graph.
- `add_edge(u, v)`: Adds an edge between nodes `u` and `v`.
- `get_neighbors(u)`: Returns a list of neighbors of node `u`.
- `vertices()`: Returns a list of vertices in the graph.

### SocialNetworkAnalyzer Class

The `SocialNetworkAnalyzer` class provides functionalities to analyze and visualize a social network graph.

#### Methods:

- `__init__(social_network)`: Initializes the social network analyzer with a given social network data.
- `build_network()`: Constructs the social network graph.
- `visualize_network()`: Visualizes the social network graph using NetworkX and Matplotlib.
- `degree_centrality()`: Calculates and prints the degree centrality of each person in the network.
- `clustering_coefficients()`: Calculates and prints the clustering coefficients of each person in the network.
- `community_detection()`: Detects and prints communities within the network using a simple approach.
- `shortest_path(source, target)`: Finds and prints the shortest path between two given people in the network.
- `interactive_analysis()`: Provides an interactive menu for users to perform various analyses on the social network graph.

## Usage

1. Clone the repository and navigate to the project directory.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the `main.py` script to start the program.
4. Follow the interactive menu to perform different analyses on the social network graph.

For detailed usage instructions, refer to the `README.md` file.

## Sample Social Network Data

The sample social network data provided in the `social_network` variable represents a small social network.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
