# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    gHead = None
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        self.gHead, mid, temp = head, head, head
        while (temp and temp.next):
            mid = mid.next
            temp = temp.next.next
        
        return self.helper(mid)
    
    def helper(self, mid):
        if not mid.next:
            return self.gHead.val == mid.val
        
        ret = self.helper(mid.next) and self.gHead.next.val == mid.val
        self.gHead = self.gHead.next
        return ret

"""
https://leetcode.com/problems/palindrome-linked-list/

Runtime: 2143 ms, faster than 10.05% of Python online submissions for Palindrome Linked List.
Memory Usage: 122.2 MB, less than 5.19% of Python online submissions for Palindrome Linked List.
"""