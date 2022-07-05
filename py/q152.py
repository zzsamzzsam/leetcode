class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = nums[0]
        prod = 1

        for i in nums:
            prod *= i
            ret = max(ret, prod)
            if prod == 0:
                prod = 1
        prod = 1
        for i in reversed(nums):
            prod *= i
            ret = max(ret, prod)
            if prod == 0:
                prod = 1
        return ret

"""
https://leetcode.com/problems/maximum-product-subarray/

Runtime: 118 ms, faster than 19.48% of Python online submissions for Maximum Product Subarray.
Memory Usage: 13.9 MB, less than 62.40% of Python online submissions for Maximum Product Subarray.
"""