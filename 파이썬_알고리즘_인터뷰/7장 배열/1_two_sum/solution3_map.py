# 52ms , 15.4MB
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [i, nums_map[target - n]]
            nums_map[n] = i


Solution().twoSum([3,3], 6)