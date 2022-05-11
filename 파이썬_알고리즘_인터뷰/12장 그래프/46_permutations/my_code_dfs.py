from copy import deepcopy
from typing import List

# deepcopy 쓰는 부분이 마음에 들지 않음
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums]

        def recursive(cand: List[int]):
            # 순열 하나 완성 -> 리턴
            if len(cand) == len(nums):
                ans.append(deepcopy(cand))
                return

            for i in nums:
                # 문제에서 구분된 integer 라고 했으므로 해당 순열에 같은 값이 있으면 continue
                if i in cand:
                    continue
                cand.append(i)
                recursive(cand)
                cand.pop()

        recursive([])
        return ans


print(Solution().permute([1]))
print(Solution().permute([0, 1]))
print(Solution().permute([1, 2, 3]))
