# 되게 감탄한 코드
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output



q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
q.push(3)
print(q.pop())