# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # leetcode solution
        if head == None:
            return None
        first = head
        second_head = second = head.next
        while first.next and second.next:
            first.next, second.next = first.next.next, second.next.next
            first = first.next
            second = second.next
        first.next = second_head
        return head

"""
https://leetcode.com/problems/odd-even-linked-list/

Runtime: 28 ms, faster than 93.35% of Python online submissions for Odd Even Linked List.
Memory Usage: 17 MB, less than 58.11% of Python online submissions for Odd Even Linked List.
"""