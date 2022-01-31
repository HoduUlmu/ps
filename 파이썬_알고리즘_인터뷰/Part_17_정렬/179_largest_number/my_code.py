from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def is_swap(num1: str, num2: str) -> bool:
            #   num1 = 3 num2 = 30
            # 330 < 303
            # false
            return num1 + num2 < num2 + num1

        if sum(nums) == 0:
            return '0'

        nums = list(map(str, nums))
        for cur in range(1, len(nums)):
            for delta in range(1, cur + 1):
                cmp = cur - delta
                if is_swap(nums[cmp], nums[cmp + 1]):
                    nums[cmp], nums[cmp + 1] = nums[cmp + 1], nums[cmp]
                else:
                    break
        print(nums)
        return ''.join(nums)


print(Solution().largestNumber([3, 30, 34, 5, 9]))
print(Solution().largestNumber(nums=[10, 2, 300, 30, 3, 412, 432, 432, 30, 9, 39, 39, 19]))
