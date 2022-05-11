# 스택으로도 구현해보려 했으나 시간초과로 실패

import collections
import sys


read = sys.stdin.readline

n, m, k, x = map(int, read().split())
graph = collections.defaultdict(list)
dist = collections.defaultdict(int)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

stack = [(x, 0)]

while stack:
    node, time = stack.pop(0)
    if node not in dist:
        dist[node] = time
        for adjust in graph[node]:
            stack.append((adjust, time + 1))


ans = [x for x in dist if dist[x] == k]
if not ans:
    print(-1)
else:
    for x in sorted(ans):
        print(x)

