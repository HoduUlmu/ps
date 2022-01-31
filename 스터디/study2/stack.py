class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if self.top is None:
            return None

        top_val = self.top.val
        self.top = self.top.nxt
        return top_val

    def is_empty(self):
        return not self.top
