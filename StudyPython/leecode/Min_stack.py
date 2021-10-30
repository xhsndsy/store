class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化一个栈
        self.A = []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> None:
        self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return min(self.A)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()