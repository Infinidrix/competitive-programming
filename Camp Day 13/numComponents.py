# https://leetcode.com/problems/linked-list-components/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        components = 0
        counts = [0 for i in range(10000)]
        sums = len(G)
        for i in G:
            counts[i] += 1
        in_chain = False
        while head:
            if counts[head.val] == 1 and not in_chain:
                in_chain = True
                components += 1
            if in_chain and counts[head.val] == 0:
                in_chain = False
            head = head.next
        return components
