class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        col = set()
        l, r = 0, 0
        long = 0
        while r < len(s):
            if s[r] not in col:
                col.add(s[r])
                long = max(len(col), long)
                r += 1
            else:
                col.remove(s[l])
                l += 1
        return long

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Runtime: 38 ms, faster than 96.18% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.6 MB, less than 85.92% of Python online submissions for Longest Substring Without Repeating Characters.
"""