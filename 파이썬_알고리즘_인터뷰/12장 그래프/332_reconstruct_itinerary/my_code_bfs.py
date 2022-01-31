import bisect
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel_dic = collections.defaultdict(collections.deque)
        for node in tickets:
            bisect.insort(travel_dic[node[0]], node[1])

        queue = collections.deque()
        queue.append('JFK')
        visited = ['JFK']

        while queue:
            front = queue.popleft()

            if not travel_dic[front]:
                break

            to = travel_dic[front].popleft()
            visited.append(to)
            queue.append(to)

        return visited


Solution().findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
Solution().findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
