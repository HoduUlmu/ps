class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class Queue:
    # 큐 초기화
    # 처음엔 front None
    def __init__(self):
        self.front = None

    # 맨 앞이 비어있다면 새 노드 생성해서 front 지정
    # 아니라면 nxt 통해 연결 리스트 끝까지 탐색 후 노드 생성
    def enqueue(self, val):
        if not self.front:
            self.front = Node(val, None)
            return

        node = self.front
        while node.nxt:
            node = node.nxt
        node.nxt = Node(val, None)

    # 맨 앞이 비어있다면 None 리턴
    # 아니라면 현 front 변수에 할당 후 리턴
    # 현 front nxt 새 front로 지정
    def dequeue(self):
        if self.front is None:
            return None

        front_val = self.front.val
        self.front = self.front.nxt
        return front_val

    # front 없으면 true, 아니면 false
    def is_empty(self):
        return not self.front
