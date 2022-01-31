from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        while head:


        def insertion_sort(lst):
            for cur in range(1, len(lst)):
                for delta in range(1, cur + 1):
                    cmp = cur - delta
                    if lst[cmp] > lst[cmp + 1]:
                        lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
                    else:
                        break
            return lst
