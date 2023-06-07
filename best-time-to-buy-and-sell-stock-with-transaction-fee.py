class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices) 
        buying = -prices[0]
        selling = 0
    

        for i in range(1, n):
            lastbuy = buying
            
            buying = max(buying, selling - prices[i])
            selling = max(selling, (prices[i] + lastbuy) - fee)

        return selling