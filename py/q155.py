class MinStack(object):

    def __init__(self):
        self.stack = []
        self.cmin = float("inf")
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.cmin = min(self.cmin, val)
        self.stack.append([val, self.cmin])
        

    def pop(self):
        """
        :rtype: None
        """
        temp = self.stack.pop()
        if not self.stack:
            self.cmin = float("inf")
        elif temp[1] == self.cmin:
            self.cmin = self.stack[-1][1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
https://leetcode.com/problems/min-stack/

Runtime: 47 ms, faster than 92.97% of Python online submissions for Min Stack.
Memory Usage: 18 MB, less than 5.49% of Python online submissions for Min Stack.
"""