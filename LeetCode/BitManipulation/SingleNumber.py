# Given a non-empty array of integers nums, every element appears 
# twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.

def singleNumber( nums):
        totalXor = nums[0]
        for i in range(1,len(nums)):
            totalXor ^= nums[i] 
        return totalXor

print(singleNumber([1,2,1,3,3,4,5,4,5]))