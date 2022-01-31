# 1623ms, 25.2MB
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_price, max_price = prices[0], prices[0]
        for price in prices:
            if price < min_price:
                min_price = price

            if price < max_price:
                max_price = price

            if price > max_price:
                max_price = price
                profit = max(profit, max_price - min_price)
        return profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])
Solution().maxProfit([7,6,4,3,1])