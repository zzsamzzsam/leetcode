# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.helper(root) != -1
    
    def helper(self, root):
        if root is None:
            return 0
        r = self.helper(root.right)
        l = self.helper(root.left)

        if r != -1 and l != -1 and abs(r-l) <= 1:
            return max(r, l) + 1
        return -1

"""
https://leetcode.com/problems/balanced-binary-tree/

Runtime: 45 ms, faster than 78.08% of Python online submissions for Balanced Binary Tree.
Memory Usage: 17.8 MB, less than 80.75% of Python online submissions for Balanced Binary Tree.
"""