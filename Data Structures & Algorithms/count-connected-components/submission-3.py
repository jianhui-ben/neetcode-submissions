from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        very typical union find and graph traversal
        time: O(E + V)
        space: O(E + V)
        """
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        out = 0
        visited = set()
        
        def dfs(i):
            if i in visited: return
            visited.add(i)
            for j in graph[i]:
                dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                out += 1
        return out