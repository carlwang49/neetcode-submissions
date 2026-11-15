from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def check_cycle(edges: list) -> bool:
            graph = defaultdict(list)

            # Build undirected graph
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            visited = set()

            # Need to check every connected component
            for node in graph:
                if node not in visited:
                    if dfs(node, -1, graph, visited):
                        return True
            return False

        def dfs(cur: int, parent: int, graph: dict, visited: set) -> bool:
            # Mark current node as visited
            visited.add(cur)

            for nxt in graph[cur]:
                if nxt not in visited:
                    if dfs(nxt, cur, graph, visited):
                        return True
                elif nxt != parent:
                    # Visited neighbor that is not parent => cycle detected
                    return True

            return False

        # Remove edges from back to front (as you did)
        for i in range(len(edges) - 1, -1, -1):
            new_edges = edges[:i] + edges[i + 1:]
            if not check_cycle(new_edges):
                return edges[i]
