from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        this is to find a cycle -> put the cycle into a set
        then reverse traversal the edges, find the edge that're in the cycle set
        """
        graph = defaultdict(list)
        n = 0
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        parent = {}
        def dfs(cur, par):
            visited.add(cur)
            parent[cur] = par
            for neighbor in graph[cur]:
                if neighbor == par:
                    continue
                if neighbor in visited:
                    cycle = [neighbor]
                    while cur != neighbor:
                        cycle.append(cur)
                        cur = parent[cur]
                    return cycle
                cycle = dfs(neighbor, cur)
                if cycle: return cycle
            return []         

        def find_last_edge(cycle):
            cycle_set = set(cycle)
            for i in range(len(edges) - 1, -1, -1):
                edge = edges[i]
                if edge[0] in cycle_set and edge[1] in cycle_set:
                    return edge
            return None

        for i in range(1, len(edges) + 1):
            if i not in visited:
                cycle = dfs(i, None)
                if cycle:
                    return find_last_edge(cycle)
        return None