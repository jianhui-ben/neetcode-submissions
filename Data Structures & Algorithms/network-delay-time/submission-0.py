import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        BFS style question
        
        1. create a min heap contain the nodes [(time_k, k)]
        2. pop the head of min heap get (time_k, K), add k in to visited set
        3, traverse the next node of K, assuming its (time_k + time_k_next_1, k_next_1) and (time_k + time_k_next_2, k_next_2)
        4, add them to the min heap, update the current out = max(out, new_time) 
        5, while loop stop when the min_heap is empty
        6, if visited set's size == n: return out, else -1
        """
        out = 0
        
        graph = defaultdict(list)
        
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        min_heap = [(0, k)]
        visited = set()
        heapq.heapify(min_heap)
        print(graph)
        while min_heap:
            cur_time_spent, cur_node = heapq.heappop(min_heap)
            if cur_node in visited:
                continue
            # print(f"processing cur_node: {cur_node}, so far takes min of {cur_time_spent} time reaching it")

            out = max(out, cur_time_spent)
            visited.add(cur_node)
            for edge in graph[cur_node]:
                next_node, edge_time = edge[0], edge[1]
                
                heapq.heappush(min_heap, (cur_time_spent + edge_time, next_node))

        return out if len(visited) == n else -1                 
            
        
        
        
        
        