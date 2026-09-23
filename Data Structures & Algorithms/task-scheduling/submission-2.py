from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
  
        """
        we use the max heap to determine which task to prioritize
        then we use a queue to track the cool down tasks
        
        in the queue we track when the taske will be completed

        """
        max_heap = [-freq for _, freq in Counter(tasks).items()]
        heapq.heapify(max_heap)
        queue = deque()
        
        cur_time = 0
        while max_heap or queue:
            if max_heap:
                freq = heapq.heappop(max_heap)
                cur_time += 1
                if freq < -1:
                    queue.append((freq + 1, cur_time + n))
            else:
                cur_time += 1
            
            ## check if any queue head has any element reaching the end of cooldown time
            if queue and queue[0][1] == cur_time:
                freq, _ = queue.popleft()
                heapq.heappush(max_heap, freq)

        return cur_time



        # """
        # math solution
        # """
        # counts = Counter(tasks).values()
        # max_freq = max(counts)
        
        # # Count how many tasks share the maximum frequency
        # num_max_freq_tasks = sum(1 for count in counts if count == max_freq)
        
        # # Calculate minimum time needed based on the most frequent task
        # ans = (max_freq - 1) * (n + 1) + num_max_freq_tasks
        
        # # If the total number of tasks is greater, we never need to idle at all
        # return max(ans, len(tasks))

      
        