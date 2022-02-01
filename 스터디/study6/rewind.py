# 트리 노드 클래스
# 왼쪽 오른쪽 자식과 value 가짐
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val,
        self.left = left
        self.right = right


# 리스트로 이진 트리 만드는 함수
def make_tree_by(lst: list, idx: int):
    # parent 초기값은 None
    # 재귀를 통해 leaf node 자식에 도달했을 떄 return 값은 None
    parent = None

    # idx가 리스트 길이 범위 내에 있을 때
    if idx < len(lst):
        value = lst[idx]
        # value None이면 리턴
        if value is None:
            return None

        # lst[idx] 저장된 값으로 트리 노드 생성
        parent = TreeNode(value)

        # 양쪽 자식을 리스트에서 idx로 찾아 재귀 호출
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    # 해당 노드 리턴
    return parent
