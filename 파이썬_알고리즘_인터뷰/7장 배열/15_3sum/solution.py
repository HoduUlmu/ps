# 1289ms, 17.4MB
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                if sum_val < 0:
                    left += 1
                elif sum_val > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results




print(Solution().threeSum([-1, 0, 1, 2, -1, 4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))
print(Solution().threeSum([0, 0]))
print(Solution().threeSum([0, 0, 0, 0, 0]))
print(Solution().threeSum([1, 2, -2, -1]))
print(Solution().threeSum([-1, 0, 1, 0]))
print(Solution().threeSum([-2, 0, 1, 1, 2]))
print(Solution().threeSum([3,0,-2,-1,1,2]))
