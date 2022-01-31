# 53ms, 14.1MB
import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        num = 0
        jewel_dic = collections.defaultdict(int)

        for char in jewels:
            jewel_dic[char] = 1

        for char in stones:
            if jewel_dic[char] == 1:
                num += 1

        return num
