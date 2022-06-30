class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:return []
        m, n = len(heights),len(heights[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited and heights[new_x][new_y]>=heights[x][y]:
                    dfs(visited, new_x,new_y)

        #iterate from left border and right border
        for i in range(m):
            dfs(p_visited,i,0)
            dfs(a_visited,i,n-1)

        #iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited,0,j)
            dfs(a_visited,m-1,j)

        #The intersections of two sets are coordinates where water can flow to both P and A
        return list(p_visited.intersection(a_visited))

"""
attempted a solution tha would check where the water from the grid would flow but there was backtracking issues
took a leetcode solution that solved by checking where the ocean water would reach
https://leetcode.com/problems/pacific-atlantic-water-flow/

Runtime: 285 ms, faster than 74.89% of Python online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.4 MB, less than 37.88% of Python online submissions for Pacific Atlantic Water Flow.
"""

"""
class Solution(object):
    def pacificAtlantic(self, heights):
        height = len(heights)
        length = len(heights[0])
        flow = [0] * height

        for i in range(height):
            flow[i] = [0] * length

        def helper(i, j, d):
            h = heights[i][j]

            if flow[i][j] == [1, 1]:
                return flow[i][j]
            
            po, ao = 0, 0
            if i == 0 or j == 0:
                po = 1
            if i == height-1 or j == length-1:
                ao = 1

            print(i, j, " |/| ", po, ao)
            if i > 0 and d != 'r' and (not po or not ao) and h >= heights[i-1][j]:
                temp = helper(i-1, j, 'l')
                po = max(temp[0], po)
                ao = max(temp[1], ao)

            if i+1 < height and d != 'l' and (not po or not ao) and h >= heights[i+1][j]:
                temp = helper(i+1, j, 'r')
                po = max(temp[0], po)
                ao = max(temp[1], ao)

            if j > 0 and d != 'd' and (not po or not ao) and h >= heights[i][j-1]:
                temp = helper(i, j-1, 'u')
                po = max(temp[0], po)
                ao = max(temp[1], ao)

            if j+1 < length and d != 'u' and (not po or not ao) and h >= heights[i][j+1]:
                temp = helper(i, j+1, 'd')
                po = max(temp[0], po)
                ao = max(temp[1], ao)
            
            flow[i][j] = [po, ao]
            return [po, ao]
        
        for i in range(height):
            for j in range(length):
                helper(i, j, '')
        
        ret = []
        for i in range(height):
            for j in range(length):
                if flow[i][j] == [1,1]:
                    ret.append([i, j])

        print(flow)
        return ret
"""