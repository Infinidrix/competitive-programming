# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        final = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
                head = head.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
                head = head.next
        if not (l2 or l1):
            return head.next
        if l2:
            l1 = l2
        while l1:
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next
        return final.next
