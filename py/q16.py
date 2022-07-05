class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        minDiff = float("inf")
        ret = 0
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s - target)
                if diff < minDiff:
                    minDiff = diff
                    ret = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target

        return ret

"""
https://leetcode.com/problems/3sum-closest/

Runtime: 6901 ms, faster than 22.49% of Python online submissions for 3Sum Closest.
Memory Usage: 13.3 MB, less than 96.36% of Python online submissions for 3Sum Closest.
"""