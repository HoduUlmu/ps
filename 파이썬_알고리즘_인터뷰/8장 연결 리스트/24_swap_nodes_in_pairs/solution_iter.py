from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next


d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
ans = Solution().swapPairs(a)

while ans is not None:
    print(ans.val)
    ans = ans.next
