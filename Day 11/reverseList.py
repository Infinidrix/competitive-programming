# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        final = head
        temp1 = head.next
        temp2 = head
        if not temp1: return head
        while temp1.next:
            temp3 = temp1.next
            temp1.next = temp2
            temp2 = temp1
            temp1 = temp3
        final.next = None
        temp1.next = temp2
        return temp1
        
            