from 파이썬_알고리즘_인터뷰.Part_14_트리.study.structures import TreeNode


def make_tree_by(lst: list, idx: int) -> TreeNode | None:
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent