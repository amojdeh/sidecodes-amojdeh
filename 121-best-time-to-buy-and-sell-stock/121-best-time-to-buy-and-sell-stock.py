class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         p = prices[:]
#         p.sort(reverse=True)
#         if prices == p:
#             return 0
#         else:
            
#             while prices.index(max(prices)) < prices.index(min(prices)):
#                 if min(prices) == prices[-1]:
#                     prices.pop(-1)
#                 else:
#                     prices.pop(prices.index(max(prices)))
#         return max(prices) - min(prices)
        n = len(prices)
        p = prices[:]
        p.sort(reverse=True)
        if prices == p:
            return 0
        else:
            lowest = prices[0]
            max_prof = 0
            
            for pr in prices:
                
                max_prof = max(max_prof, pr - lowest)
                lowest = min(pr,lowest)
            return max_prof
            
            