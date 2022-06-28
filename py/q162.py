class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, len(nums)-1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

"""
https://leetcode.com/problems/find-peak-element/solution/

Runtime: 61 ms, faster than 14.81% of Python online submissions for Find Peak Element.
Memory Usage: 13.6 MB, less than 67.14% of Python online submissions for Find Peak Element.
"""