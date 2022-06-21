class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        x = len(matrix[0])
        y = len(matrix)

        up, left = 0, 0
        right = x
        down = y
        dir = 'right'

        ret = []

        while (up != down and left != right):
            obj = self.helper(matrix, up, right, down, left, dir)
            arr = obj[0]
            dir = obj[1]
            up, right, down, left = obj[2]

            ret += arr
        
        return ret
            

    def helper(self, matrix, up, right, down, left, dir):
        ret = []
        if (dir == 'right'):
            for i in range(left, right):
                ret.append(matrix[up][i])
            dir = 'down'
            up += 1
        elif (dir == 'down'):
            for i in range(up, down):
                ret.append(matrix[i][right-1])
            dir = 'left'
            right -= 1
        elif (dir == 'left'):
            for i in range(right-1, left-1, -1):
                ret.append(matrix[down-1][i])
            dir = 'up'
            down -= 1
        elif (dir == 'up'):
            for i in range(down-1, up-1, -1):
                ret.append(matrix[i][left])
            dir = 'right'
            left += 1
        return [ret, dir, [up, right, down, left]]

"""
https://leetcode.com/problems/spiral-matrix/

Runtime: 9 ms, faster than 98.53% of Python online submissions for Spiral Matrix.
Memory Usage: 13.3 MB, less than 68.52% of Python online submissions for Spiral Matrix.
"""