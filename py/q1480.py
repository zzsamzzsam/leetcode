class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        numSize = len(nums)
        ret = [0] * numSize
        ret[0] = nums[0]
        for i in range(1, numSize):
            ret[i] = ret[i-1] + nums[i]

        return ret

"""
https://leetcode.com/problems/running-sum-of-1d-array/

Runtime: 45 ms, faster than 31.59% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.4 MB, less than 84.35% of Python online submissions for Running Sum of 1d Array.
"""