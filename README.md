# Homework – Graph Traversal Algorithms (DFS & BFS)

## Task 2: Comparison of DFS and BFS Algorithms

###  Description

In this task, a graph representing a real-world transport network was used to analyze and compare two fundamental graph traversal algorithms:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**

The goal was to find paths between two vertices in the graph and compare the results produced by each algorithm.

---

### Graph Model

- **Type:** Undirected graph  
- **Vertices:** Transport stations  
- **Edges:** Direct connections between stations  

The same graph structure from Task 1 was reused to ensure a fair comparison between the algorithms.

---

###  Algorithm Results

#### Breadth-First Search (BFS)
- Explores the graph **level by level**
- Always finds the **shortest path in terms of number of edges**
- Suitable for problems where optimal (shortest) paths are required

**Result:**  
BFS returned the shortest possible path between the start and destination nodes.

---

#### Depth-First Search (DFS)
- Explores the graph by going **as deep as possible** along one branch before backtracking
- Does **not guarantee the shortest path**
- The resulting path depends heavily on the order of node traversal

**Result:**  
DFS produced a longer and less optimal path, which may include unnecessary detours.

---

###  Comparison of DFS and BFS

| Criterion | BFS | DFS |
|--------|-----|-----|
| Traversal strategy | Breadth-first | Depth-first |
| Shortest path guarantee | Yes |  No |
| Dependence on node order | Low | High |
| Path optimality | Optimal | Arbitrary |

---

###  Explanation of Differences

The difference in the resulting paths is explained by the nature of the algorithms:

- **BFS** examines all neighboring nodes first, ensuring that the first time a destination is reached, the path is the shortest possible.
- **DFS** prioritizes depth over optimality and may explore long paths before reaching the target, even if shorter paths exist.

As a result, BFS is more suitable for shortest-path problems, while DFS is better suited for exhaustive exploration tasks.

---

###  Conclusion

The comparison demonstrates that:

- **BFS** is the preferred algorithm when the shortest path is required.
- **DFS** does not guarantee optimal paths but can be useful for exploring all possible routes.

The observed differences in paths are a direct consequence of the traversal strategies used by each algorithm.

---


