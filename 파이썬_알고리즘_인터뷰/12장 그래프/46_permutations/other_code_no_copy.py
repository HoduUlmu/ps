from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        board = [0] * len(nums)

        def recursive(cand, length):
            if length >= len(nums):
                ans.append(cand)
                return

            for i in range(len(nums)):
                if board[i]:
                    continue
                board[i] = 1
                recursive(cand + [nums[i]], length + 1)
                board[i] = 0

        recursive([], 0)
        return ans


print(Solution().permute([1]))
print(Solution().permute([0, 1]))
print(Solution().permute([1, 2, 3]))
