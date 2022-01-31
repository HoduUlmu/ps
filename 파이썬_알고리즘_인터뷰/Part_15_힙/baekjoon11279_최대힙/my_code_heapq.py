import heapq
import sys

read = sys.stdin.readline
n = int(read())
heap = []

for i in range(n):
    control = int(read())
    if control == 0:
        print(0) if not heap else print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -control)
