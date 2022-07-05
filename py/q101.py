# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(l, r):
            if l is None and r is None:
                return True
            elif l is None or r is None or l.val != r.val:
                return False
            if l.val == r.val:
                return helper(l.left, r.right) and helper(l.right, r.left)
        
        return helper(root.left, root.right)

"""
https://leetcode.com/problems/symmetric-tree/

Runtime: 16 ms, faster than 96.78% of Python online submissions for Symmetric Tree.
Memory Usage: 13.8 MB, less than 17.26% of Python online submissions for Symmetric Tree.
"""