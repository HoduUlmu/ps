import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        dist = [sys.maxsize] * n
        dist[src] = 0

        q = []
        heapq.heappush(q, (0, src, k))

        while q:
            acc, cur, cur_k = heapq.heappop(q)

            if cur_k < 0:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                dist[adj] = cost
                heapq.heappush(q, (cost, adj, cur_k - 1))

        return dist[dst] if dist[dst] != sys.maxsize else -1


# print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
# print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
print(Solution().findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1))
