import java.util.Scanner;
class TwoSum{
    public static int[] twoSum(int[] nums, int target) {
        int[] numbers = new int[2];
        for (int i=0; i<nums.length; i++){
            for (int j=i+1; j<nums.length; j++){
                if (nums[i] + nums[j] == target){
                    numbers[0] = i;
                    numbers[1] = j;
					System.out.println("here "+i+" "+j+ " " + numbers[1]);
                }
            }
        }
        return numbers;
    }
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int[] nums = new int[4];
		int target = in.nextInt();
		nums[0] = in.nextInt();
		nums[1] = in.nextInt();
		nums[2] = in.nextInt();
		nums[3] = in.nextInt();
		System.out.println(""+twoSum(nums, target)[0] + twoSum(nums, target)[1]);
	}
}