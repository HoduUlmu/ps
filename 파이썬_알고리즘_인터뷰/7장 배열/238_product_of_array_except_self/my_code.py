# timeout
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums) - 1):
                top = nums.pop(0)
                mul *= top
                nums.append(top)
            result.append(mul)

        return result[::-1]


print(Solution().productExceptSelf([1, 2, 3, 4]))
