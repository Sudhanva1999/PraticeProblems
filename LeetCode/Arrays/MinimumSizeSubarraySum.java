public class MinimumSizeSubarratSum {
  public int minSubArrayLen(int target, int[] nums) {
    Arrays.sort(nums);
    int sum = 0;
    int len = 0;
    for(int i : nums) {
      sum += i;
      len++;
      if(sum == target) {
        return len;
      }
      if(sum > target) {
        sum -= i;
        len --;
        continue;
      }
    }
    return 0;
  }
  public static void main() {
    int[] array1 = [2,3,1,2,4,3];
    int ans = minSubArrayLen(7, array1);
  }

}