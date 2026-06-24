class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        option 1: convert into a map and then compare the map
        option 2: sorting the string and then compare the sorted string, not ideal
        """
        # from collections import Counter
        # return Counter(s) == Counter(t)
        
        return sorted(s) == sorted(t)