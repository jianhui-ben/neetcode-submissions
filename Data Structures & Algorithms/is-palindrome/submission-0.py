class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        two pointer:
        left and right, if left and right are alphanuemric, then check if they are the same after changing to lower case
        '''
        s_lower_case = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s_lower_case[left].isalnum():
                left += 1

            while left < right and not s_lower_case[right].isalnum():
                right -= 1

            if left < right and s_lower_case[left] != s_lower_case[right]:
                return False
            left += 1
            right -= 1

        return True