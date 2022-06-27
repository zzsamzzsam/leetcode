class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        # Redefine n to be max tasks per cycle
        n += 1
        
        # Collect tasks into a dictionary to count frequencies
        dic = {}
        for x in tasks:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        
        # Find the frequency of the largest bottlneck
        bneck = 0
        # And how many tasks have that frequency
        bnecks = 1
        for x in dic.values():
            if x > bneck:
                bneck = x
                bnecks = 1
            elif x == bneck:
                bnecks += 1
        
        return max(len(tasks), n * (bneck - 1) + bnecks)


"""
https://leetcode.com/problems/task-scheduler/

Runtime: 528 ms, faster than 72.04% of Python online submissions for Task Scheduler.
Memory Usage: 15.4 MB, less than 95.10% of Python online submissions for Task Scheduler.


"""