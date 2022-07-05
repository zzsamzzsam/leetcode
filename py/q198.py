class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        p1, p2 = 0, 0
        for n in nums:
            t = p1
            p1 = max(p2 + n, p1)
            p2 = t
        
        return p1

"""
https://leetcode.com/problems/house-robber/

Runtime: 35 ms, faster than 22.00% of Python online submissions for House Robber.
Memory Usage: 13.5 MB, less than 42.07% of Python online submissions for House Robber.
"""