class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        exahasutively listing all possible partitions, when any part is not
        palindrome, stop early
        """
        
        out = []

        def isPadlindrome(s):
            left, right = 0, len(s) - 1
            
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True

        def backtracking(cur_list, start_idx):
            if start_idx >= len(s):
                out.append(list(cur_list))
                return
            
            for j in range(start_idx, len(s)):
                if isPadlindrome(s[start_idx: j + 1]):
                    cur_list.append(s[start_idx: j + 1])
                    backtracking(cur_list, j + 1)
                    cur_list.pop()



        backtracking([], 0)

        return out