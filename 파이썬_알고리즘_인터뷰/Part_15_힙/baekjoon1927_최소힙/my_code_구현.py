import sys


class BinaryMinHeap:
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
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[smallest] > self.items[left]:
            smallest = left

        if right <= len(self) and self.items[smallest] > self.items[right]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)


def control(c):
    if c == 0:
        print(min_heap.extract())
    else:
        min_heap.insert(c)


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    min_heap = BinaryMinHeap()
    for i in range(n):
        control(int(read()))
