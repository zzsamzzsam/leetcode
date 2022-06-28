# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) <= 0:
            return None

        mid = int(len(nums)/2)

        tn = TreeNode()
        tn.val = nums[mid]
        tn.left = self.sortedArrayToBST(nums[:mid])
        tn.right = self.sortedArrayToBST(nums[mid+1:])

        return tn
        
"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Runtime: 118 ms, faster than 23.44% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.1 MB, less than 73.68% of Python online submissions for Convert Sorted Array to Binary Search Tree.
"""