# Given an array of positive integers arr, return the sum of 
# all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

def sumOddLengthSubarrays(arr):
    sumArr = 0 
    for i,num in enumerate(arr):
        sumArr += ((((i + 1) * (len(arr) - i) + 1) // 2) * num) 
    return sumArr
print(sumOddLengthSubarrays([1,4,2,5,3]))