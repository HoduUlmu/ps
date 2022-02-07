import heapq
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        dist = [sys.maxsize] * (n + 1)
        q = []

        heapq.heappush(q, (0, k))
        dist[k] = 0

        while q:
            acc, cur = heapq.heappop(q)

            if dist[cur] < acc:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))
        dist = dist[1:]
        return -1 if any(sys.maxsize == d for d in dist) else max(dist)


Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
print(Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
