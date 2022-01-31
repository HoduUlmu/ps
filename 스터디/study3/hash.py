import collections


# key 와 value를 가지며 다음 ListNode를 참조하는 ListNode 클래스
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    # size 1000으로 초기화
    # 해쉬테이블은 defaultdict, value값을 ListNode로 선언
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 새 key와 value 삽입
    def put(self, key: int, value: int) -> None:
        # index는 키값을 사이즈로 나눈 나머지 (해쉬 함수)
        index = key % self.size

        # 만약 현재 인덱스가 해쉬테이블에서 비어있다면 ListNode 생성 후 해당 인덱스에 할당
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 해당 인덱스에 값이 있다면 연결 리스트 형태 이므로 끝까지 탐색한 후 그 뒤에 ListNode 생성 후 할당
        p = self.table[index]
        while p:
            # 같은 키값을 가진 노드가 있다면 업데이트
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)

    # 키 값을 이용해 value 조회
    def get(self, key: int) -> int:
        index = key % self.size

        # 인덱스를 통해 조회 시 값이 없다면 -1 리턴
        if self.table[index].value is None:
            return -1

        p = self.table[index]

        # ListNode를 돌며 같은 키 값을 가진 노드가 있으면 해당 value 리턴, 없으면 -1 리턴
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 키값으로 노드 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        # 인덱스 비어있으면 리턴
        if self.table[index].value is None:
            return

        # 삭제하려는 노드가 맨 처음일 경우
        # 하나만 있다면 빈 노드 할당
        # 뒤에 연결된 노드가 있다면 다음 노드를 맨 앞으로 할당 후 리턴
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
