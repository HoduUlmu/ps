#51ms, 14.2MB
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left
            # if node.left and node.right:
            #     node.left, node.right = node.right, node.left
            #
            # elif node.left:
            #     node.right = node.left
            #     node.left = None
            #
            # elif node.right:
            #     node.left = node.right
            #     node.right = None

        dfs(root)

        return root


e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3)
b = TreeNode(2, left=d, right=e)
a = TreeNode(1, left=b, right=c)
Solution().invertTree(a)

print(a.left.val)
print(a.right.val)
print(a.right.right.val)