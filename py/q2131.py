class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        dict = {}

        for w in words:
            if w not in dict:
                if w[::-1] not in dict:
                    dict[w] = [1, 0]
                else:
                    dict[w[::-1]][1] += 1
            else:
                dict[w][0] += 1
        
        sum = 0
        mid = False
        for word in dict:
            if word[0] == word[1]:
                count = dict[word][0]
                if not mid and count % 2 == 1:
                    mid = True
                    sum += 2
                sum += (int(count/2) * 4)
            else:
                count = min(dict[word][0], dict[word][1])
                sum += (count * 4)
        return sum
"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

Runtime: 2172 ms, faster than 11.63% of Python online submissions for Longest Palindrome by Concatenating Two Letter Words.
Memory Usage: 37.5 MB, less than 86.05% of Python online submissions for Longest Palindrome by Concatenating Two Letter Words.
"""