class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(t) > len(s):
            return ""
        if t == s:
            return t
        
        s += " "
        l, r = 0, 0
        diff = len(s)
        pos = []
        missing = t
        extras = ""
        while r < len(s):
            if missing:
                if s[r] in missing:
                    i = missing.index(s[r])
                    missing = missing[:i] + missing[i+1:]
                elif s[r] in t:
                    extras += s[r]
                r += 1
            else:
                if r-l < diff:
                    diff = r-l
                    pos = [l,r]
                if s[l] in t:
                    if s[l] in extras:
                        i = extras.index(s[l])
                        extras = extras[:i] + extras[i+1:]
                    else:
                        missing += s[l]
                l += 1
        
        if pos:
            return s[pos[0]:pos[1]]
        else:
            return ""

"""
https://leetcode.com/problems/minimum-window-substring/

Runtime: 690 ms, faster than 8.94% of Python online submissions for Minimum Window Substring.
Memory Usage: 14.2 MB, less than 70.52% of Python online submissions for Minimum Window Substring.
"""