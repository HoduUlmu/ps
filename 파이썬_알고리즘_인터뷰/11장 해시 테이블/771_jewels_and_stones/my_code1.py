import collections

# 70ms, 14.2MB
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        num = 0

        for char in stones:
            if char in jewels:
                num += 1

        return num
