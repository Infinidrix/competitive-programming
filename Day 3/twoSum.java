class Solution {
	//https://leetcode.com/problems/two-sum/
	
    public int[] twoSum(int[] nums, int target) {
        int[] numbers = new int[2];
        for (int i=0; i<nums.length; i++){
            for (int j=i+1; j<nums.length; j++){
                if (nums[i] + nums[j] == target){
                    numbers[0] = i;
                    numbers[1] = j;
                    return numbers;
                }
            }
        }
        return numbers;
    }
}