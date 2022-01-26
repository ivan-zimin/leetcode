class MinStackSlow:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def __repr__(self):
        return str(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0 or self.minimum[-1] > val:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(-1)
    obj.pop()
    print(obj.top())
    print(obj.getMin())