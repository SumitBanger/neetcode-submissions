class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.minStack.pop()
        self.mainStack.pop()
            
    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
