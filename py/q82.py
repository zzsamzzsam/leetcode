# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        ln = ListNode(0)
        ret = ln
        prev = head.val
        add = True
        while head.next is not None:
            head = head.next
            if head.val == prev:
                add = False
            else:
                if add:
                    tn = ListNode(prev)
                    ln.next = tn
                    ln = ln.next
                prev = head.val
                add = True

        if add:
            tn = ListNode(head.val)
            ln.next = tn
        return ret.next

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Runtime: 61 ms, faster than 11.11% of Python online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.7 MB, less than 12.62% of Python online submissions for Remove Duplicates from Sorted List II.
"""