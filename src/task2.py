import networkx as nx
from collections import deque


def build_transport_graph() -> nx.Graph:
    G = nx.Graph()

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


def bfs_path(graph: nx.Graph, start: str, goal: str) -> list[str]:
    """
    Breadth-First Search: finds shortest path (by number of edges)
    """
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []


def dfs_path(graph: nx.Graph, start: str, goal: str) -> list[str]:
    """
    Depth-First Search: explores deep paths first
    """
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return []


def main():
    graph = build_transport_graph()

    start = "Central"
    goal = "Airport"

    bfs_result = bfs_path(graph, start, goal)
    dfs_result = dfs_path(graph, start, goal)

    print("BFS path:")
    print(" -> ".join(bfs_result))

    print("\nDFS path:")
    print(" -> ".join(dfs_result))


if __name__ == "__main__":
    main()
