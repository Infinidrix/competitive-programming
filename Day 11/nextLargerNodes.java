/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// https://leetcode.com/problems/next-greater-node-in-linked-list/

import java.util.ArrayList;

class Solution {
    public int[] nextLargerNodes(ListNode head) {
        int cacheMax = 0;
        ArrayList<Integer> nextLarger = new ArrayList<Integer>();
        if (head==null) return new int[] {};
        while(head!=null){
            cacheMax = 0;
            if (head.val < cacheMax) nextLarger.add(cacheMax);
            else{
                int largerVal = 0;
                ListNode check = head;
                while(check!=null){
                    if (head.val < check.val){
                        cacheMax = check.val;
                        largerVal = check.val;
                        break;
                    }
                    check = check.next;
                }
                if (largerVal > 0) nextLarger.add(cacheMax);
                else nextLarger.add(0);
            }
            head = head.next;
        }
        int[] returner = nextLarger.stream().mapToInt(i -> i).toArray();
        return returner;
    }
}
