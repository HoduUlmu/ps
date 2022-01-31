
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revere(node: Optional[ListNode], prev: Optional[ListNode] = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return revere(next, node)

        return revere(head)


e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
ans = Solution().reverseList(a)
