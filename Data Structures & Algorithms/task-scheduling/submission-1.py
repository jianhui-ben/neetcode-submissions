from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        max_freq = max(counts)
        
        # Count how many tasks share the maximum frequency
        num_max_freq_tasks = sum(1 for count in counts if count == max_freq)
        
        # Calculate minimum time needed based on the most frequent task
        ans = (max_freq - 1) * (n + 1) + num_max_freq_tasks
        
        # If the total number of tasks is greater, we never need to idle at all
        return max(ans, len(tasks))
        # """
        # we use the max heap to determine which task to prioritize
        # then we use a queue to track the cool down tasks
        # """
        # max_heap = [(-freq, key) for key, freq in Counter(tasks).items()]
        # heapq.heapify(max_heap)
        # queue = deque()
        
        # out = 0
        # wait_turns = 0
        # while max_heap or queue:
        #     if max_heap:
        #         freq, task = heapq.heappop(max_heap)
        #         if freq < -1:
        #             queue.append((freq + 1, task))
        #         else:
        #             queue.append((0, None))
        #     else:
        #         queue.append((0, None))
        #     out += 1

        #     # EARLY EXIT: If the heap is empty, and we haven't queued 
        #     # any actual remaining tasks, we are finished!
        #     # (Checking any(f < 0 for f, t in queue) ensures no unfinished tasks are left)
        #     if not max_heap and not any(f < 0 for f, t in queue):
        #         break
            
        #     if len(queue) > n:
        #         freq, task = queue.popleft()
        #         if freq:
        #             heapq.heappush(max_heap, (freq, task))
        # return out

        