import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

        # [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        # [['JFK', 'MUC'], ['LHR', 'SFO'], ['MUC', 'LHR'], ['SFO', 'SJC']]
        # [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", ""JFK], ["ATL", "SFO"]]

        route, stack = [], ['JFK']

        # [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


Solution().findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
Solution().findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
