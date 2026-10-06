class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        typical backtracking

        1. create a map {num : list(letters ...)}
        2. for each digit, do backtracking(cur_str, cur_idx)
        time: O(3 ** N)
        space: O(N)
        """
        out = []
        
        digit_to_letter = [
            [],                      # 0
            [],                      # 1
            ["a", "b", "c"],         # 2
            ["d", "e", "f"],         # 3
            ["g", "h", "i"],         # 4
            ["j", "k", "l"],         # 5
            ["m", "n", "o"],         # 6
            ["p", "q", "r", "s"],    # 7
            ["t", "u", "v"],         # 8
            ["w", "x", "y", "z"]     # 9
        ]
        
        def backtracking(cur_str, cur_idx):
            if cur_idx == len(digits):
                out.append(cur_str)
                return
            for letter in digit_to_letter[int(digits[cur_idx])]:
                backtracking(cur_str + letter, cur_idx + 1)
        if not digits: return []
        backtracking("", 0)
        return out