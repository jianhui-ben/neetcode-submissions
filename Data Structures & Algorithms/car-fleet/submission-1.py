class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        how to determine two cars, i and j, merge into a fleet:
        
        assuming i < j
        if target - position[j] / speed[j] >= target - position[i] / speed[i]:
            then i and j merge
        else:
            keep track of the time
        """
        
        sorted_pos_and_speed = [(position[i], speed[i]) for i in range(len(position))]
        sorted_pos_and_speed.sort(key=lambda x: -x[0])
        arrival_times = []
        
        for pos, sp in sorted_pos_and_speed:
            arrival_time = (target - pos) / sp
            if not arrival_times or arrival_time > arrival_times[-1]:
                arrival_times.append(arrival_time)

        return len(arrival_times)
        