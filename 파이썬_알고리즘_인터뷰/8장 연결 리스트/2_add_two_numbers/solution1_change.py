# 165ms, 14.4MB
import functools
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def to_list(self, node: ListNode) -> List:
        list: List = []

        while node:
            list.append(node.val)
            node = node.next
        return list

    def to_reversed_linked_list(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        # result_str = int(''.join(map(str, a))) + int(''.join(map(str, b)))
        result_str = functools.reduce(lambda x, y: 10 * x + y, a, 0) + \
                     functools.reduce(lambda x, y: 10 * x + y, b, 0)
        return self.to_reversed_linked_list(str(result_str))
