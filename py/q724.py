class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rSum = sum(nums)
        lSum = 0
        for i in range(len(nums)):
            mid = nums[i]
            rSum -= mid
            if (lSum == rSum):
                return i
            lSum += mid
        return -1

"""
https://leetcode.com/problems/find-pivot-index/

Runtime: 228 ms, faster than 33.99% of Python online submissions for Find Pivot Index.
Memory Usage: 14.4 MB, less than 84.55% of Python online submissions for Find Pivot Index.
"""