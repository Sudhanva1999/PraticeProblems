# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Elegant
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} 
        for i, num in enumerate(nums):
            r = target - num 
            if( r in d):
                return [d[r], i]
            d[num] = i

# Non Elegant
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ind1 = 0 
#         ind2 = 0 
#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if(i == j):
#                     continue 
#                 if((num1 + num2) == target):
#                     ind1 = i 
#                     ind2 = j
#         return [ind1, ind2]
            
