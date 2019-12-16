// https://leetcode.com/problems/intersection-of-two-arrays/submissions/

import java.util.ArrayList;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> result = new ArrayList<>();
        for (int i:nums1){
            if (result.contains(i)){
                continue;
            }
            for (int k:nums2){
                if (k==i){
                    result.add(i);
                    break;
                }
            }
        }
        int[] num = new int[result.size()];
        for(int i = 0; i<result.size();i++){
            num[i] = result.get(i);
        }
        return num;
    }
}
