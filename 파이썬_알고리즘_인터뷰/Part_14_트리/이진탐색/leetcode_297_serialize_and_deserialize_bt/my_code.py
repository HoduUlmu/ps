from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return []

        queue = deque([root])
        lst = []
        while queue:
            node = queue.popleft()
            lst.append(node.val)

            if node.left and node.right:
                queue.append(node.left)
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)
                lst.append(None)
            elif node.right:
                queue.append(node.right)
                lst.append(None)
            else:
                lst.append(None)
                lst.append(None)

            return lst


    def deserialize(self, data):
        if not data:
            return

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
