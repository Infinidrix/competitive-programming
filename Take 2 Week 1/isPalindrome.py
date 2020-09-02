
# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None: return True
        length = 1
        prev = head
        next = head.next
        while next != None:
            length += 1
            next.prev = prev
            prev = next
            next = next.next
        start = head
        end = prev
        while length >= 2:
            if start.val != end.val:
                return False
            start = start.next
            end = end.prev
            length -= 2
        return True