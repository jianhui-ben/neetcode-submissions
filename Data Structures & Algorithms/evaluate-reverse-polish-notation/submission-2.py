class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators_set = set(["-", "+", "*", "/"])
        for token in tokens:
            if token not in operators_set:
                stack.append(token)
            else:
                num_2, num_1 = int(stack.pop()), int(stack.pop())
                if token == "+":
                    new_num = num_1 + num_2
                elif token == "-":
                    new_num = num_1 - num_2
                elif token == "*":
                    new_num = num_1 * num_2
                elif token == "/":
                    new_num = num_1 / num_2
                stack.append(new_num)
        return int(stack[0])