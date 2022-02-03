class BinaryMaxHeap:
    # 힙 초기화
    # 인덱스 계산 편의를 위해 None을 넣어 1부터 사용
    def __init__(self):
        self.items = [None]

    # 힙 길이는 items 리스트의 길이 - 1로 설정 (None 값 제외)
    def __len__(self):
        return len(self.items) - 1

    # 삽입되는 값을 맨 뒤로 넣어주고 힙을 다시 재정렬
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 값을 뺄 때는 맨 앞과 맨 뒤를 스왑 후 pop
    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    # 삽입 시 힙 재정렬
    def _percolate_up(self):
        # 삽입된 값은 맨 뒤에 있으므로 cur는 현 힙의 길이로 설정
        cur = len(self)
        parent = cur // 2

        # 부모보다 현재 노드가 더 크면 스왑
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    # 추출 시 힙 재정렬
    def _percolate_down(self, cur):
        # 맨 위에 삽입 후 자식을 탐색
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # biggest가 달라졌으면 스왑 후 재귀
        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)
