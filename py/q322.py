class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0

        dp=[amount] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)

        return -1 if dp[-1]==amount else dp[-1]

"""
the idea of dp is solving from the bottom up
line 15 checks if itself is already the most optimal or if the current amount (i) minus the current coin value's optimal coin count plus one is more optimal
all previous indices are already optimal
https://leetcode.com/problems/coin-change/

Runtime: 1864 ms, faster than 26.59% of Python online submissions for Coin Change.
Memory Usage: 13.7 MB, less than 94.35% of Python online submissions for Coin Change.
"""