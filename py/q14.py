class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        test = strs[0]
        i = 1
        while i < len(strs) and len(test) > 0:
            test = self.helper(test, strs[i])
            i += 1
        return test
        
    def helper(self, str1, str2):
        ret = ''
        minLen = min(len(str1), len(str2))
        i = 0
        while i < minLen and str1[i] == str2[i]:
            ret += str1[i]
            i += 1 
        return ret


"""
https://leetcode.com/problems/longest-common-prefix/

Runtime: 58 ms, faster than 6.51% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.5 MB, less than 96.16% of Python online submissions for Longest Common Prefix.
"""