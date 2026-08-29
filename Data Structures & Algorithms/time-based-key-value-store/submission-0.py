class TimeMap:

    """
    for each key, save a array of timestamp and an array of values
    for each get timestamp t1
    find the index i of last timestamp t <= t1, and return the corresponding value[i]
    """

    def __init__(self):
        self.key_to_times = {}
        self.key_to_values = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_to_times:
            self.key_to_times[key].append(timestamp)
            self.key_to_values[key].append(value)
        else:
            self.key_to_times[key] = [timestamp]
            self.key_to_values[key] = [value]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_times: return ""
        timestamps = self.key_to_times[key]
        
        left, right = 0, len(timestamps) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if timestamps[mid] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or timestamps[right] > timestamp:
            return ""
        return self.key_to_values[key][right]
