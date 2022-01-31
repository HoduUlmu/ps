from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quicksort(start, end):
            def partition(ps, pe):
                pivot = nums[pe]
                i = ps - 1

                for j in range(ps, pe):
                    if nums[j] <= pivot:
                        i += 1
                        nums[j], nums[i] = nums[i], nums[j]

                nums[i + 1], nums[pe] = nums[pe], nums[i + 1]
                return i + 1

            if start >= end:
                return None

            p = partition(start, end)
            quicksort(start, p - 1)
            quicksort(p + 1, end)
            return nums

        quicksort(0, len(nums) - 1)

Solution().sortColors([2,0,2,1,1,0])
