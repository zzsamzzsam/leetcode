class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        j = 1
        for i in range(1, len(nums)):
            if (nums[i] > nums[i-1]):
                nums[j] = nums[i]
                j += 1
        
        return j

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Runtime: 88 ms, faster than 66.79% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.9 MB, less than 44.29% of Python online submissions for Remove Duplicates from Sorted Array.
"""