# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        hold = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(hold)
        return root

"""
https://leetcode.com/problems/invert-binary-tree/

Runtime: 16 ms, faster than 90.91% of Python online submissions for Invert Binary Tree.
Memory Usage: 13.5 MB, less than 21.10% of Python online submissions for Invert Binary Tree.
"""