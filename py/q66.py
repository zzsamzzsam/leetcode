class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits.insert(0, 0)

        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if (digits[i] >= 10):
                digits[i] = 0
            else:
                break
        if (digits[0] == 0):
            digits.pop(0)
        return digits

"""
https://leetcode.com/problems/plus-one

Runtime: 27 ms, faster than 54.58% of Python online submissions for Plus One.
Memory Usage: 13.4 MB, less than 42.94% of Python online submissions for Plus One.
"""