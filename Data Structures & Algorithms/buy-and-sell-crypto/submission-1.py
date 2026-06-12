class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxProfit = 0, 0, 0

        while r <= len(prices) - 1:
            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit

            if prices[l] <= prices[r]:
                r += 1
            else:
                l += 1
        
        return maxProfit

        