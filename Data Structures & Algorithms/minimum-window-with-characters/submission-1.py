from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window to track the substring's counter
        """

        counter_t = Counter(t)
        needed = len(counter_t)
        left = right = 0
        out = s + "a"
        cur_window = Counter()
        
        while right < len(s):
            cur_window[s[right]] += 1
            if s[right] in counter_t and cur_window[s[right]] == counter_t[s[right]]:
                needed -= 1
            right += 1

            while not needed:
                ## we need to first record the current output and then shrink
                if right - left <= len(out):
                    out = s[left: right]
                cur_window[s[left]] -= 1
                if s[left] in counter_t and cur_window[s[left]] < counter_t[s[left]]:
                    needed += 1
                left += 1
                
        return out if len(out) <= len(s) else ""
