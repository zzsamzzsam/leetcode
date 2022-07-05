class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = sum(nums)
        if s % 2:
            return False
        
        s = int(s/2)
        arr = [False] * (s+1)
        arr[0] = True

        for n in nums:
            if arr[s]:
                break
            for i in range(s, n-1, -1):
                arr[i] = arr[i] or arr[i-n]

        return arr[s]

"""
problem redux to finding if half of sum is possible with any combination of n in nums
line 17 iteration is descending cuz cant repeat use any n in nums

https://leetcode.com/problems/partition-equal-subset-sum/

Runtime: 705 ms, faster than 73.21% of Python online submissions for Partition Equal Subset Sum.
Memory Usage: 13.7 MB, less than 96.62% of Python online submissions for Partition Equal Subset Sum.
"""