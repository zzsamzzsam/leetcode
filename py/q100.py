# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def helper(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None or n1.val != n2.val:
                return False
            else:
                return helper(n1.left, n2.left) and helper(n1.right, n2.right)
        
        return helper(p, q)

"""
https://leetcode.com/problems/same-tree/

Runtime: 29 ms, faster than 36.02% of Python online submissions for Same Tree.
Memory Usage: 13.4 MB, less than 87.11% of Python online submissions for Same Tree.
"""