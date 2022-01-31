# 42ms, 14.4MB
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 = [1,2,4] list2 = [1,3,4]
        # if list1 is None and list2 is None:
        #     print("현재", "list1 value = None", "list2 value = None")
        # elif list1 is None:
        #     print("현재", "list1 value = None", "list2 value = ", list2.val)
        # else:
        #     print("현재", "list1 value = ", list1.val, "list2 value = ", list2.val)

        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

            # if list1 is None and list2 is None:
            #     print("스왑 후", "list1 value = None", "list2 value = None")
            # elif list2 is None:
            #     print("현재", "list1 value = ", list1.val, "list2 value = None")
            # else:
            #     print("스왑 후", "list1 value = ", list1.val, "list2 value = ", list2.val)

        if list1:
            # print("재귀호출")
            list1.next = self.mergeTwoLists(list1.next, list2)
            # if list1.next is not None:
            #     # print(list1.val,"의 next는", list1.next.val)
            # else:
            #     print(list1.val, "의 next는 None")

        # print("리턴")
        return list1


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
