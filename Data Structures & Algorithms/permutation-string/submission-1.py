from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        maintain the substring into dict
        """

        left, right = 0, 0
        cur_window = {}
        s1_dict = dict(Counter(s1))

        while right < len(s2):
            cur_window[s2[right]] = cur_window.get(s2[right], 0) + 1
            right += 1
            
            while right - left > len(s1):
                cur_window[s2[left]] -= 1
                if not cur_window[s2[left]]:
                    cur_window.pop(s2[left])
                left += 1
            if cur_window == s1_dict:
                return True
        return False