class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        ret = []

        for i in range(len(grid[0])):
            x = i
            y = 0
            cur = grid[y][x]
            while y <= len(grid):
                if (y == len(grid)):
                    ret.append(x)
                    break

                cur = grid[y][x]

                if (x + cur < 0 or x + cur >= len(grid[0])):
                    ret.append(-1)
                    break

                side = grid[y][x+cur]

                if (side + cur == 0):
                    ret.append(-1)
                    break

                y += 1
                x += cur
        return ret

"""
https://leetcode.com/problems/where-will-the-ball-fall/

Runtime: 234 ms, faster than 40.74% of Python online submissions for Where Will the Ball Fall.
Memory Usage: 13.6 MB, less than 88.89% of Python online submissions for Where Will the Ball Fall.
"""