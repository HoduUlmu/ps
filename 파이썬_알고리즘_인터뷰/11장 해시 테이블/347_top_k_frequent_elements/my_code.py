# 159ms, 18.6MB
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        ans = [x[0] for x in freqs.most_common(k)]
        return ans

