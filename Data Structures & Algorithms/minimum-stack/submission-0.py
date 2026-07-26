class MinStack:

    """
    for getMin(), we don't need to worry anything bigger than the current min if that's
    pushed latest than the current min
    so we need to have a regular list, plus a descresing monotonic stack to keep the min
    """

    def __init__(self):
        self.full_list = []
        self.desc_stack = []
        

    def push(self, val: int) -> None:
        self.full_list.append(val)
        if not self.desc_stack or val <= self.desc_stack[-1]:
            self.desc_stack.append(val)


    def pop(self) -> None:
        cur_val = self.full_list.pop()
        if cur_val == self.desc_stack[-1]:
            self.desc_stack.pop()

    def top(self) -> int:
        return self.full_list[-1]
        

    def getMin(self) -> int:
        return self.desc_stack[-1]
        
