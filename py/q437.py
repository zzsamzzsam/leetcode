# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count = 0
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        self.count = 0
        self.helper(root, targetSum, [])
        return self.count

    def helper(self, root, t, arr):
        if root is None:
            return
        
        if root.val == t:
            self.count += 1
            
        for i in range(len(arr)):
            v = root.val + arr[i]
            if v == t:
                self.count += 1
            arr[i] = v
        
        self.helper(root.right, t, arr + [root.val])
        self.helper(root.left, t, arr + [root.val])

"""
https://leetcode.com/problems/path-sum-iii/

Runtime: 406 ms, faster than 46.55% of Python online submissions for Path Sum III.
Memory Usage: 30.9 MB, less than 7.47% of Python online submissions for Path Sum III.
"""