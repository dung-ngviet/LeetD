from typing import List

# Solution 1: Brute force
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxPro = 0
#         if len(prices) < 2: return maxPro

#         for i in range(0, len(prices) -  1):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > maxPro: maxPro = profit
#         return maxPro


# Solution 2: DP
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                current_profit = prices[i] - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([1,2]))