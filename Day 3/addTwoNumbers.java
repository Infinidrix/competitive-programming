# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	// https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summ = ListNode(0)
        hello = summ
        carry = 0
        while l1 and l2:
            result = l1.val + l2.val + carry
            summ.val = (result)%10
            carry = result//10
            summ.next = ListNode(0)
            temp = summ
            summ = summ.next
            l1, l2 = l1.next, l2.next
            
        if l1 and not l2:
            l2 = l1
        while l2:
            result = l2.val + carry
            summ.val = (result)%10
            carry = result//10
            summ.next = ListNode(0)
            temp = summ
            summ = summ.next
            l2 = l2.next
        if carry != 0:
            summ.val = carry
        else:
            temp.next = None
            
        return hello
            
            