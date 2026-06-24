class MyQueue:

    def __init__(self):
        self.inStack = []
        self.ouStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.ouStack:
            while self.inStack:
                self.ouStack.append(self.inStack.pop())

        return self.ouStack.pop()

    def peek(self) -> int:
        if not self.ouStack:
            while self.inStack:
                self.ouStack.append(self.inStack.pop())

        return self.ouStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.ouStack