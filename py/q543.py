# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ret = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
        
    def helper(self, root):
        if root is None:
            return 0
        
        rh = self.helper(root.right)
        lh = self.helper(root.left)

        self.ret = max(self.ret, rh+lh)

        return max(rh, lh) + 1

"""
https://leetcode.com/problems/diameter-of-binary-tree/

Runtime: 29 ms, faster than 93.37% of Python online submissions for Diameter of Binary Tree.
Memory Usage: 16.1 MB, less than 85.53% of Python online submissions for Diameter of Binary Tree.
"""