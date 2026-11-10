from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        create an adjacency map
        for each vertice, do a dfs traversal and update the counter
        time: O(V + E)
        space: O (V + E) 
        """
        graph = defaultdict(set)
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].add(b)
            graph[b].add(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            next_nodes = list(graph[node])
            for next_node in next_nodes:
                graph[next_node].discard(node)
                graph[node].discard(next_node)
                dfs(next_node)
            return


        out = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                out += 1
        return out
        
