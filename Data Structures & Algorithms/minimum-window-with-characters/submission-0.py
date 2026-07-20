from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window to track the substring's counter
        """

        def is_inclusive(sub_counter, main_counter):
            # Subtracting removes keys with 0 or negative counts
            return not (sub_counter - main_counter)

        counter_t = Counter(t)
        left = right = 0
        out = s + "a"
        cur_window = Counter()
        
        while right < len(s):
            cur_window[s[right]] += 1
            right += 1
            
            while is_inclusive(counter_t, cur_window):
                if right - left <= len(out):
                    out = s[left: right]
                cur_window[s[left]] -= 1
                left += 1
        return out if len(out) <= len(s) else ""
