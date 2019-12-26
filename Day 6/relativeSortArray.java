// https://leetcode.com/problems/relative-sort-array/submissions/

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int max = arr1[0];
        for (int num:arr1){
            if (max < num){
                max = num;
            }
        }
        for (int i = 1; i < arr1.length; i++){
            int temp = arr1[i];
            int j = 0;
            while (i-1-j>=0 && greaterThan(arr1[i-1-j], arr1[i-j], arr2, max)){
                arr1[i-j] = arr1[i-j-1];
                arr1[i-j-1] = temp;
                j++;
            }
            arr1[i-j] = temp;
        }
        return arr1;
    }
    public boolean greaterThan(int a, int b, int[] comp, int max){
        int count = 0;
        int a_index = Integer.MAX_VALUE - max + a;
        int b_index = Integer.MAX_VALUE - max + b;
        for (int num:comp){
            if (num == a){
                a_index = count;
            }
            if(num == b){
                b_index = count;
            }
            count++;
        }
        return (a_index>b_index);
    }
}
