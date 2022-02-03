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
        if not self.top:
            return None

        top_node_val = self.top.val
        self.top = self.top.nxt
        return top_node_val

    def is_empty(self):
        return not self.top


class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        if not self.front:
            self.front = Node(val, None)
            return

        node = self.front
        while node.nxt:
            node = node.nxt
        node.nxt = Node(val, None)

    def pop(self):
        if not self.front:
            return None

        front_node_val = self.front.val
        self.front = self.front.nxt