# 786ms, 15.4MB
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 이거 근데 테스트 케이스 추가되면 탈락될 수도
# 오른쪽과 왼쪽의 depth가 같고 왼쪽에 더 깊은 경로가 있을 때 답이 안나올 수 있다
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def find_max_depth(node):
            if not node:
                return 0

            q = deque([node])
            depth = 0

            while q:
                depth += 1
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return depth

        max_depth = 0
        while root:
            left = find_max_depth(root.left)
            right = find_max_depth(root.right)
            cur_depth = left + right
            max_depth = max(cur_depth, max_depth)
            root = root.left if left > right else root.right

        return max_depth


e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3)
b = TreeNode(2, left=d, right=e)
a = TreeNode(1, left=b, right=c)
print(Solution().diameterOfBinaryTree(a))
