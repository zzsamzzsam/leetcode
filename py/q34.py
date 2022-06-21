class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left, right = 0, len(nums)-1
        if (right < 0):
            return [-1, -1]
        while left != right and nums[left] <= target and target < nums[right]:
            left += 1 if nums[left] < target else 0
            right -= 1 if target < nums[right] else 0

        return [left, right] if nums[left] == target else [-1, -1]

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Runtime: 133 ms, faster than 9.37% of Python online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.2 MB, less than 99.73% of Python online submissions for Find First and Last Position of Element in Sorted Array.
"""