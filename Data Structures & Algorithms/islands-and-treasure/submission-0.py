class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        BFS:
        initialize the queu [cordinates of each tresure chest]
        and then go to each of 4 directions, 
        for each new coordinates, 
            if it's <= 0 then stop
            else, update the min(each coordinate's value, current step)
        add new coordinates into the queue

        stop while the queue is empty
        
        time: O(n)
        space: O(n)
        """
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dis = 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = (1 << 31) - 1
        while queue:
            new_queue = []
            for r, c in queue:
                for del_r, del_c in dirs:
                    new_r, new_c = r + del_r, c + del_c
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == INF:
                        grid[new_r][new_c] = dis
                        new_queue.append((new_r, new_c))
            dis += 1
            queue = new_queue

        return






                





