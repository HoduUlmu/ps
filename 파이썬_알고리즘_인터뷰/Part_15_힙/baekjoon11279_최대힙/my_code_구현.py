import sys


class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return 0

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] <= self.items[parent]:
                break
            self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[biggest] < self.items[left]:
            biggest = left

        if right <= len(self) and self.items[biggest] < self.items[right]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)


def control(c):
    if c == 0:
        print(max_heap.extract())
    else:
        max_heap.insert(c)


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    max_heap = BinaryMaxHeap()

    for _ in range(n):
        control(int(read()))