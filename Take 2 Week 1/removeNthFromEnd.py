
# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        remove_node, end_node, dist = head, head, 0
        
        while end_node.next != None:
            end_node = end_node.next
            dist += 1
            if dist > n:
                remove_node = remove_node.next
                dist -= 1
            #print(f"end: {end_node.val}, dist: {dist} and curr: {remove_node.val}")
        
        if dist == n - 1 and remove_node == head:
            return head.next
        
        remove_node.next = remove_node.next.next
        
        return head
            