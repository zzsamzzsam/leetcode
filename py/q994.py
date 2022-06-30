class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid[0])
        height = len(grid)
        fresh, minute = 0, 0
        rottenXY = []
        for i in range(height):
            for j in range(length):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rottenXY.append([i, j])

        while fresh > 0 and rottenXY:
            tempXY = rottenXY
            newRotten = []
            for ij in tempXY:
                i, j = ij
                adjs = []

                if i > 0:
                    adjs.append((i-1,j))
                if i+1 < height:
                    adjs.append((i+1,j))
                if j > 0:
                    adjs.append((i,j-1))
                if j+1 < length:
                    adjs.append((i,j+1))

                for a in adjs:
                    ai, aj = a
                    if grid[ai][aj] == 1:
                        grid[ai][aj] = 2
                        newRotten.append([ai, aj])
                        fresh -= 1

            rottenXY = newRotten
            minute += 1
        
        return -1 if fresh > 0 else minute

"""
https://leetcode.com/problems/rotting-oranges/

Runtime: 48 ms, faster than 64.73% of Python online submissions for Rotting Oranges.
Memory Usage: 13.6 MB, less than 19.42% of Python online submissions for Rotting Oranges.
"""