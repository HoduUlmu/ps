# 57ms, 14.2MB
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        first_pointer = ans

        while list1 and list2:
            if list1.val < list2.val:
                ans.next = list1
                ans = ans.next
                list1 = list1.next
            else:
                ans.next = list2
                ans = ans.next
                list2 = list2.next

        ans.next = list1 or list2

        return first_pointer.next


c2 = ListNode(4)
b2 = ListNode(3, c2)
a2 = ListNode(1, b2)

c = ListNode(4)
b = ListNode(2, c)
a = ListNode(1, b)
ans = Solution().mergeTwoLists(a, a2)

while ans is not None:
    print(ans.val)
    ans = ans.next
