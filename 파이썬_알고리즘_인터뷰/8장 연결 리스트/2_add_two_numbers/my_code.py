# 114ms, 14.3MB
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = ''
        l2_num = ''

        while l1:
            l1_num += str(l1.val)
            l1 = l1.next
        l1_num = int(l1_num[::-1])

        while l2:
            l2_num += str(l2.val)
            l2 = l2.next
        l2_num = int(l2_num[::-1])

        sum_num = str(l1_num + l2_num)

        prev = None
        for num in sum_num:
            node = ListNode(int(num), prev)
            prev = node

        return prev


c = ListNode(3)
b = ListNode(4, c)
a = ListNode(2, b)

c2 = ListNode(4)
b2 = ListNode(6, c2)
a2 = ListNode(5, b2)

ans = Solution().addTwoNumbers(a, a2)
while ans is not None:
    print(ans.val)
    ans = ans.next
