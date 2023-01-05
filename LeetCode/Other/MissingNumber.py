# Given an array nums containing n distinct numbers in 
# the range [0, n], return the only number in the range
#  that is missing from the array.

def missingNumber(nums):
        return ((len(nums) * (len(nums)+ 1)) // 2) - sum(nums)

print(missingNumber([0,1]))