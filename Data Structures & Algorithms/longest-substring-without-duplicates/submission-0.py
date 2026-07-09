class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window to check a set
        [left, right + 1] -> a set
        if s[right] in the set:
            then shrink the window by incrementing left
            until s[left] == s[right], then left += 1
        """
        left = right = 0
        existed = set()
        out = 0
        while right < len(s):
            if s[right] not in existed:
                existed.add(s[right])
                right += 1
                out = max(out, right - left)
            else:
                while s[left] != s[right]:
                    existed.remove(s[left])
                    left += 1
                existed.remove(s[left])
                left += 1

        return out
        
        