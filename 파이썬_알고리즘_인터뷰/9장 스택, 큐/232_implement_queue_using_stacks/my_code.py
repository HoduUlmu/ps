# 56ms, 14.2MB
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())
        self.stack.append(x)

        while tmp:
            self.stack.append(tmp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack



q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())