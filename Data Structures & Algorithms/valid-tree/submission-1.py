from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        a valid tree:

        1. all nodes are connected (this is easy)
        2. there's no circle

        I can just do dfs to traverse every single node:
        check 1. if there's a edge connecting to this vertice
              2. do a dfs traversel, update visited and current_path
        """

        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        visited = set()        
        def dfs(node):
            if node in visited:
                return True
            
            visited.add(node)
            next_nodes = list(graph[node])
            for next_node in next_nodes:
                
                graph[node].remove(next_node)
                graph[next_node].remove(node)
                if dfs(next_node):
                    return True
            return False
        
        find_cycle = dfs(0)
        return not find_cycle and len(visited) == n