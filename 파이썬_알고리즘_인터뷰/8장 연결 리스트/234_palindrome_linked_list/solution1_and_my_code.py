# 1837ms, 47.4MB
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        node = head

        while node is not None:
            q.append(node)
            node = node.next

        while len(q) > 1:
            if q.pop(0).val != q.pop().val:
                return False

        return True


d = ListNode(1)
c = ListNode(2, d)
b = ListNode(2, c)
a = ListNode(1, b)
print(Solution().is_palindrome(a))
