class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self.trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t["-"] = True
        print(self.trie)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for c in word:
            if c not in t: return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for c in prefix:
            if c not in t: return False
            t = t[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
https://leetcode.com/problems/implement-trie-prefix-tree/

Runtime: 152 ms, faster than 94.60% of Python online submissions for Implement Trie (Prefix Tree).
Memory Usage: 29.6 MB, less than 87.79% of Python online submissions for Implement Trie (Prefix Tree).
"""