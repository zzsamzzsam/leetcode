class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        s = set()

        while (n not in s):
            s.add(n)
            n = self.sumSqDigits(n)
            if (n == 1):
                return True
        return False

    def sumSqDigits(self, n):
        sum = 0
        while(n > 0):
            digit = n % 10
            sum += (digit**2)
            n = n // 10
        return sum

"""
https://leetcode.com/problems/happy-number/

Runtime: 34 ms, faster than 42.79% of Python online submissions for Happy Number.
Memory Usage: 13.2 MB, less than 85.10% of Python online submissions for Happy Number.
"""