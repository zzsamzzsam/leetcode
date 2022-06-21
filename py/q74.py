class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        search = []
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                search = matrix[i]
                break
        
        for i in range(len(search)):
            if target < search[i]:
                return False
            if target == search[i]:
                return True
        
        return False

"""
https://leetcode.com/problems/search-a-2d-matrix/

Runtime: 58 ms, faster than 14.34% of Python online submissions for Search a 2D Matrix.
Memory Usage: 13.6 MB, less than 92.86% of Python online submissions for Search a 2D Matrix.
"""