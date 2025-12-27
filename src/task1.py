import networkx as nx
import matplotlib.pyplot as plt


def build_transport_graph() -> nx.Graph:
    """
    Builds a transport network graph.
    Nodes represent stations.
    Edges represent direct connections between stations.
    """
    G = nx.Graph()

    # Add stations (nodes)
    stations = [
        "Central",
        "University",
        "Airport",
        "Stadium",
        "Museum",
        "Park",
        "Old Town"
    ]
    G.add_nodes_from(stations)

    connections = [
        ("Central", "University"),
        ("Central", "Museum"),
        ("University", "Stadium"),
        ("Stadium", "Airport"),
        ("Museum", "Old Town"),
        ("Old Town", "Park"),
        ("Park", "Central"),
        ("Museum", "Park"),
    ]
    G.add_edges_from(connections)

    return G


def analyze_graph(G: nx.Graph) -> None:
    """
    Prints basic graph characteristics.
    """
    print("Graph analysis:")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print("\nNode degrees:")
    for node, degree in G.degree():
        print(f"  {node}: {degree}")


def visualize_graph(G: nx.Graph) -> None:
    """
    Visualizes the graph.
    """
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        font_size=10,
        edge_color="gray"
    )
    plt.title("City Transport Network")
    plt.show()


def main():
    graph = build_transport_graph()
    analyze_graph(graph)
    visualize_graph(graph)


if __name__ == "__main__":
    main()
