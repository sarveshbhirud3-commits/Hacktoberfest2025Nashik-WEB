from collections import defaultdict, deque
from typing import List, Tuple

def longest_path_dag(n: int, edges: List[Tuple[int, int]]) -> Tuple[int, List[int]]:
    """
    Returns (length, path) of the longest path in a DAG.
    Nodes are 0-indexed.
    """
    graph = defaultdict(list)
    indeg = [0]*n
    for u,v in edges:
        graph[u].append(v)
        indeg[v] += 1

    # 1️⃣ Topological sort using Kahn’s algorithm
    topo = []
    q = deque([i for i in range(n) if indeg[i] == 0])
    while q:
        node = q.popleft()
        topo.append(node)
        for nei in graph[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)

    # 2️⃣ DP to find longest path
    dist = [-float('inf')]*n
    parent = [-1]*n
    for node in topo:
        if dist[node] == -float('inf'):
            dist[node] = 0  # starting node
        for nei in graph[node]:
            if dist[nei] < dist[node] + 1:
                dist[nei] = dist[node] + 1
                parent[nei] = node

    # 3️⃣ Find the endpoint of the longest path
    end_node = max(range(n), key=lambda x: dist[x])
    length = dist[end_node]

    # 4️⃣ Reconstruct path
    path = []
    while end_node != -1:
        path.append(end_node)
        end_node = parent[end_node]
    path.reverse()

    return length, path

# Example usage
if __name__ == "__main__":
    n = 6
    edges = [
        (0, 1), (0, 2),
        (1, 3), (2, 3),
        (3, 4), (4, 5)
    ]
    length, path = longest_path_dag(n, edges)
    print("Longest path length:", length)
    print("Path:", path)
