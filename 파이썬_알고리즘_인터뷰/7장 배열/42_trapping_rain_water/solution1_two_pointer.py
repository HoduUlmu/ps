# 112ms, 15.7MB
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left_pointer, right_pointer = 0, len(height) - 1
        left_max, right_max = height[left_pointer], height[right_pointer]
        volume = 0

        while left_pointer < right_pointer:
            left_max = max(height[left_pointer], left_max)
            right_max = max(height[right_pointer], right_max)

            if left_max <= right_max:
                volume += left_max - height[left_pointer]
                left_pointer += 1
            else:
                volume += right_max - height[right_pointer]
                right_pointer -= 1

        return volume