# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []

        ret = []
        ret.append(root.val)

        def helper(n, h):
            if n is None:
                return
            if len(ret) < h:
                ret.append(n.val)
            else:
                ret[h-1] = n.val
            helper(n.left, h+1)
            helper(n.right, h+1)
        
        helper(root.left, 2)
        helper(root.right, 2)
        return ret

"""
https://leetcode.com/problems/binary-tree-right-side-view/

Runtime: 31 ms, faster than 45.19% of Python online submissions for Binary Tree Right Side View.
Memory Usage: 13.4 MB, less than 50.88% of Python online submissions for Binary Tree Right Side View.
"""