class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ret = -1
        if target >= nums[0]:
            for i in range(len(nums)):
                if nums[i] == target:
                    ret = i
                    break
                if target < nums[i] or (i > 0 and nums[i] < nums[i-1]):
                    break
        else:
            for i in reversed(range(len(nums))):
                if nums[i] == target:
                    ret = i
                    break
                if target > nums[i] or (i < len(nums)-1 and nums[i] > nums[i+1]):
                    break
        return ret

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

Runtime: 48 ms, faster than 25.46% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.7 MB, less than 65.48% of Python online submissions for Search in Rotated Sorted Array.
"""