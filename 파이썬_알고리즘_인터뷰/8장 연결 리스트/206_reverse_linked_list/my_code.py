# 45ms, 15.6MB
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None

        while head:
            ans, head.next, head = head, ans, head.next

        return ans



e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
ans = Solution().reverseList(a)
while ans is not None:
    print(ans.val)
    ans = ans.next
