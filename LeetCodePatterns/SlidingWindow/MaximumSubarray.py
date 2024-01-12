class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] 
        currentSum = 0 

        for num in nums :
            currentSum = max(num, currentSum + num)
            maxSum = max(currentSum, maxSum)

        return maxSum