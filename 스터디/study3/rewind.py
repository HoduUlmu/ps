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

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, val):
        if self.front is None:
            self.front = Node(val, None)
            return

        node = self.front
        while node.nxt:
            node = node.nxt
        node = node.nxt