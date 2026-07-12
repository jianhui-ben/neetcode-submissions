from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window to track a window [left, right)
        track a Counter for the window, plus a maxFreq
        while right - left - maxFreq > k: shrink the window by incrementing left
        """

        maxFreq, cnt, out = 0, Counter(), 0
        left = right = 0
        while right < len(s):
            cnt[s[right]] += 1
            maxFreq = max(maxFreq, cnt[s[right]])
            right += 1
            
            while right - left - maxFreq > k: 
                cnt[s[left]] -= 1                    
                left += 1

            out = max(out, right - left)

        return out
            