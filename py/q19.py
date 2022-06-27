# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        temp = ListNode(0, head)
        ret = temp
        i = 1
        while head.next is not None:
            head = head.next
            i += 1
            if i > n:
                temp = temp.next
        temp.next = temp.next.next
        return ret.next

"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Runtime: 32 ms, faster than 40.38% of Python online submissions for Remove Nth Node From End of List.
Memory Usage: 13.7 MB, less than 15.40% of Python online submissions for Remove Nth Node From End of List.
"""