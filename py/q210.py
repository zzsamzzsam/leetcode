class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        s = set(range(numCourses))
        highDict, lowDict = {}, {}

        for p in prerequisites:
            high = p[0]
            low = p[1]

            if high not in highDict:
                highDict[high] = set()
                if high in s:
                    s.remove(high)
            highDict[high].add(low)

            if low not in lowDict:
                lowDict[low] = set()
            lowDict[low].add(high)
        
        ret = []
        while len(s):
            c = s.pop()
            ret.append(c)

            if c in lowDict:
                highs = lowDict[c]
                for h in highs:
                    highDict[h].remove(c)
                    if len(highDict[h]) <= 0:
                        s.add(h)
        
        return ret if len(ret) == numCourses else []

"""
https://leetcode.com/problems/course-schedule-ii/

Runtime: 162 ms, faster than 19.10% of Python online submissions for Course Schedule II.
Memory Usage: 15.5 MB, less than 53.09% of Python online submissions for Course Schedule II.
"""