class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack
        """
        bracket_map = {"}" : "{", ")" : "(", "]" : "["}
        stack = []
        for c in s:
            if not stack or c not in bracket_map:
                stack.append(c)
            elif stack[-1] != bracket_map[c]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
            
        


        

        
