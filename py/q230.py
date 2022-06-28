# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ret = 0
    c = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        self.ret = 0
        self.helper(root,k)
        return self.ret
    
    def helper(self, root, k):
        if root is None:
            return

        self.helper(root.left, k)
        self.c += 1
        if self.c == k:
            self.ret = root.val
            return
        elif self.c > k:
            return
        self.helper(root.right, k)

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Runtime: 56 ms, faster than 57.68% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 21 MB, less than 81.88% of Python online submissions for Kth Smallest Element in a BST.
"""