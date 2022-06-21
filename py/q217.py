class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = set(nums)
        return len(s) != len(nums)

"""
https://leetcode.com/problems/contains-duplicate/

Runtime: 393 ms, faster than 86.47% of Python online submissions for Contains Duplicate.
Memory Usage: 23.8 MB, less than 77.55% of Python online submissions for Contains Duplicate.
"""