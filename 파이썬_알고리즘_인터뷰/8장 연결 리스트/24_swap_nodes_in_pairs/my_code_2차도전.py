# 5월 11일 2차
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = fast = slow = head
        head = head.next

        while fast and fast.next:
            fast = fast.next.next
            prev.next = slow.next
            slow.next.next, slow.next = slow, fast
            prev, slow = slow, fast

        return head


d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
Solution().swapPairs(a)
