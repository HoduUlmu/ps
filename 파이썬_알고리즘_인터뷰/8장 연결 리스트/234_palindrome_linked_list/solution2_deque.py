# 828ms, 47.6MB
import collections
from typing import Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()

        node = head

        while node is not None:
            q.append(node)
            node = node.next

        while len(q) > 1:
            if q.popleft().val != q.pop().val:
                return False

        return True
