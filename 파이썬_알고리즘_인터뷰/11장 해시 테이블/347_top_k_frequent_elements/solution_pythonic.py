# 150ms, 18.7MB
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> tuple[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(Solution().topKFrequent([1,1,1,2,2,3],2))