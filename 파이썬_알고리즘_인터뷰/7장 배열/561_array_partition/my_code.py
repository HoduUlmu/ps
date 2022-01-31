# 272ms, 16.8MB
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans


print(Solution().arrayPairSum([1, 4, 3, 2]))
print(Solution().arrayPairSum([6,2,6,5,1,2]))
