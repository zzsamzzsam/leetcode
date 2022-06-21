class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        p = prices[0]
        profit = 0 - p
        for i in range(1, len(prices)):
            if (prices[i] < prices[i-1]):
                profit += (prices[i-1] - prices[i])
                p = prices[i]
        profit += prices[-1]

        return profit

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

Runtime: 65 ms, faster than 46.67% of Python online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.5 MB, less than 41.45% of Python online submissions for Best Time to Buy and Sell Stock II.
"""