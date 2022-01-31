# 192ms, 34800KB
import collections
import sys
from typing import Deque


def printer_queue():
    # 입력
    n, m = sys.stdin.readline().split()  # 6 0
    n, m = int(n), int(m)
    doc = sys.stdin.readline().split()  # 1 1 9 1 1 1
    queue: Deque = collections.deque()

    # 큐에 데이터 삽입
    for i in range(n):
        node = [int(doc[i]), i]
        queue.append(node)

    idx = 1  # 뽑힌 순서
    while queue:
        max_val = max(queue, key=lambda x: x[0])  # 현재 큐의 최대값을 알아냄
        front = queue.popleft()

        if front == max_val:
            if front[1] == m:
                print(idx)
                break
            idx += 1
            continue

        queue.append(front)


t = int(sys.stdin.readline())
for i in range(t):
    printer_queue()
