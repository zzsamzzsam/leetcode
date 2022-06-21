import math
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # a leetcode submittion
        s = [0] * (len(num1) + len(num2))

        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mult = int(num1[i]) * int(num2[j])
                summ = mult + s[i + j + 1]
                s[i + j] += summ // 10
                s[i + j + 1] = summ % 10

        # removes leading 0s by getting the first index of a non 0 which is stored in i
        for i, c in enumerate(s):
            if c != 0:
                break
        return ''.join(map(str, s[i:]))

        """ my solution
        if num1 == '0' or num2 == '0':
            return '0'
        
        table = {}

        ret = []
        i = 0
        for n in reversed(num1):
            if (n == '0'):
                i += 1
                continue
            val = table[n] if n in table else self.multiplySingle(n, num2)
            table[n] = val
            val = val.ljust(len(val) + i, '0')
            ret.append(val)
            i += 1
        return self.addStringArray(ret)

    def multiplySingle(self, digit, num):
        ret = []
        i = 0
        for n in reversed(num):
            val = str(int(n) * int(digit))
            val = val.ljust(i + len(val), '0')
            ret.append(val)
            i += 1
        return self.addStringArray(ret)
    
    def addStringArray(self, arr):
        sum = arr[0]
        for i in range(1, len(arr)):
            sum = self.addString(sum, arr[i])
        return sum
    
    def addString(self, num1, num2):
        ret = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        carryover = 0
        for i in range(max(len(num1), len(num2)) + 1):
            d1 = '0' if i >= len(num1) else num1[i]
            d2 = '0' if i >= len(num2) else num2[i]
            val = int(d1) + int(d2) + carryover
            carryover = math.floor(val / 10)
            val = int(val % 10)
            ret += str(val)
        ret = ret.rstrip('0')[::-1]
        return ret
    """

"""
https://leetcode.com/problems/multiply-strings/

Runtime: 2897 ms, faster than 5.03% of Python online submissions for Multiply Strings.
Memory Usage: 13.5 MB, less than 51.83% of Python online submissions for Multiply Strings.
"""