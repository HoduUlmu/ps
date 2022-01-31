from typing import Optional

# 다중할당에 너무 집착했다
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        node1 = head
        ans = node2 = head.next

        while node2:
            prev, node1.next, node2.next = node1, node2.next, node1
            prev, node1, node2 = node1, node1.next, node1.next.next

        return ans


d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
ans = Solution().swapPairs(a)

while ans is not None:
    print(ans.val)
    ans = ans.next
