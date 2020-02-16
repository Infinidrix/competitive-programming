# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        prev_node = None
        curr_node1 = head
        curr_node2 = head.next
        result = head.next
        
        while curr_node1 and curr_node2:
                curr_node1.next = curr_node2.next
                curr_node2.next = curr_node1
                if prev_node:
                    prev_node.next = curr_node2
                prev_node = curr_node1
                curr_node1 = curr_node1.next
                if not curr_node1:
                    break
                curr_node2 = curr_node1.next
        return result
