class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn_price = float('inf')
        mx_profit = 0
        for i in range(len(prices)):
            mn_price = min(mn_price, prices[i])
            mx_profit = max(mx_profit, prices[i] - mn_price)
        return mx_profit        
