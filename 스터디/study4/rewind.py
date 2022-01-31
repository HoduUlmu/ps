import collections


class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.nxt = None


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
        node.nxt = Node(val, None)

    def dequeue(self):
        if self.front is None:
            return None

        front_val = self.front.val
        self.front = self.front.nxt
        return front_val

    def is_empty(self):
        return not self.front


class HashTable:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, val: int):
        index = key % self.size

        if self.table[index].val is None:
            self.table[index] = ListNode(key, val)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.val = val
                return
            if p.nxt is None:
                break

            p = p.nxt

        p.nxt = ListNode(key, val)

    def get(self, key: int):
        index = key % self.size

        if self.table[index].val is None:
            return -1

        p = self.table[index]
