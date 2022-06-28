# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.stackAdd(root)
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack

    def hasNext(self):
        """
        :rtype: bool
        """
        temp = self.stack.pop()
        self.stackAdd(temp.right)
        return temp.val
    
    def stackAdd(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
https://leetcode.com/problems/binary-search-tree-iterator/

Runtime: 108 ms, faster than 33.52% of Python online submissions for Binary Search Tree Iterator.
Memory Usage: 22.1 MB, less than 35.62% of Python online submissions for Binary Search Tree Iterator.
"""