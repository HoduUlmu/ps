import collections
import heapq
import sys


read = sys.stdin.readline

n, m, k, x = map(int, read().split())
graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

q = [(0, x)]

while q:
    time, node = heapq.heappop(q)
    if time > k:
        break
    if node not in dist:
        dist[node] = time
        for adjust in graph[node]:
            heapq.heappush(q, (time + 1, adjust))


ans = [x for x in dist if dist[x] == k]
if not ans:
    print(-1)
else:
    for x in sorted(ans):
        print(x)

