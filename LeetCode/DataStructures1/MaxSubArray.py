# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and 
# return its sum.
# A subarray is a contiguous part of an array.
def maxSubArray(nums):
    maxSum = -99999
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
        
    return maxSum 

print(maxSubArray(list(map(int,input("Enter an array to find max sum sub array.\n").split()))))