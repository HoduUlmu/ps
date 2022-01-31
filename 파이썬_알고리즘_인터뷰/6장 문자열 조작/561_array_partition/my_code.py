from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_pair = []
        ans = 0

        for idx, num in enumerate(nums):
            if (idx + 1) % 2 == 0:
                ans += min(min_pair)
                min_pair = []
            else:
                min_pair.append(num)
        return ans



print(Solution().arrayPairSum([1,4,3,2]))