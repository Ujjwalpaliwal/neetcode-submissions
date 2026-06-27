class MinStack:

    def __init__(self):
        self.main_stack:List[int]=[]
        self.min_stack:List[int]=[]
        
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val<= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        popped_val = self.main_stack.pop()
        if popped_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:

        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
