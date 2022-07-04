class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        if source == target:
            return 0

        stops, links = {}, {}
        for i in range(len(routes)):
            route = routes[i]
            for r in route:
                if r not in stops:
                    stops[r] = [i]
                else:
                    stops[r].append(i)
        
        for i in range(len(routes)):
            route = routes[i]
            s = set()
            for r in route:
                for stop in stops[r]:
                    s.add(stop)
            links[i] = s

        visited = set()
        goTo = stops[source]
        found = False
        ret = 0

        def helper(goTo):
            conns = set()
            for gt in goTo:
                if gt not in visited:
                    visited.add(gt)
                    for route in routes[gt]:
                        if target == route:
                            return True
                        else:
                            conns.update(stops[route])
            return list(conns)
        
        while True:
            ret += 1
            goTo = helper(goTo)
            if goTo == True:
                found = True
                break
            elif not goTo:
                break

        return ret if found else -1

"""
https://leetcode.com/problems/bus-routes/

Runtime: 445 ms, faster than 93.33% of Python online submissions for Bus Routes.
Memory Usage: 33.6 MB, less than 61.54% of Python online submissions for Bus Routes.
"""