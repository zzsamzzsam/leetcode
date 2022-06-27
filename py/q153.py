class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        mid = int(right / 2)
        while mid != right and mid != left:
            l = nums[left]
            r = nums[right]
            m = nums[mid]

            if m <= l:
                right = mid
            else:
                left = mid
            mid = int((right+left) / 2)
        
        return min(nums[left], nums[right])

"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Runtime: 45 ms, faster than 30.86% of Python online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.7 MB, less than 56.71% of Python online submissions for Find Minimum in Rotated Sorted Array.
"""