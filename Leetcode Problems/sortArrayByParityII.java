// https://leetcode.com/problems/sort-array-by-parity-ii/submissions/

class Solution {
    public int[] sortArrayByParityII(int[] A) {
        for (int i = 0; i < A.length; i++){
            if (i%2 != A[i]%2){
                int j;
                for (j = i+1; j < A.length; j++){
                    if (i%2 == A[j]%2){
                        break;
                    }
                }
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        return A;
    }
}
