import heapq
import networkx as nx


def build_weighted_transport_graph() -> nx.Graph:
    """
    Builds a weighted transport graph.
    Edge weights represent travel time (minutes).
    """
    G = nx.Graph()

    edges = [
        ("Central", "University", 5),
        ("Central", "Museum", 7),
        ("University", "Stadium", 4),
        ("Stadium", "Airport", 10),
        ("Museum", "Old Town", 6),
        ("Old Town", "Park", 3),
        ("Park", "Central", 8),
        ("Museum", "Park", 4),
    ]

    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)

    return G


def dijkstra(graph: nx.Graph, start: str) -> tuple[dict, dict]:
    """
    Dijkstra algorithm.
    Returns:
        distances: shortest distance from start to every node
        previous: previous node in the shortest path
    """
    distances = {node: float("inf") for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous: dict, start: str, goal: str) -> list[str]:
    """
    Reconstructs path from start to goal using the 'previous' map.
    """
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path if path[0] == start else []


def main():
    graph = build_weighted_transport_graph()
    start = "Central"

    distances, previous = dijkstra(graph, start)

    print(f"Shortest distances from '{start}':")
    for node, distance in distances.items():
        print(f"  {node}: {distance} minutes")

    print("\nShortest paths:")
    for node in graph.nodes:
        if node != start:
            path = reconstruct_path(previous, start, node)
            print(f"  {start} -> {node}: {' -> '.join(path)}")


if __name__ == "__main__":
    main()
