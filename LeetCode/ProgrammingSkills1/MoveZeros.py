# Given an integer array nums, move all 0's to the end of it while
#  maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while(i < len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
            i += 1 

        i = count
        while(i <= len(nums)-1):
            nums[i] = 0
            i += 1
        return nums

print(moveZeroes([0,1,0,3,12]))


# MY SOLUTION NON OPTIMISED 
# def moveZeroes(nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         flag2 = 1
#         for i, num in enumerate(nums):
#             if(i == len(nums) - 1 or flag2 == 0):
#                 break
#             if(num == 0):
#                 count += 1
#                 flag = 1
#                 k = i+1
#                 while(flag == 1):
#                     if(k == len(nums)-1 and nums[k] == 0):
#                         flag2 = 0 
#                         break
#                     if(nums[k] != 0):
#                         flag = 0
#                         break
#                     k += 1 
#                 nums[i] = nums[k]
#                 nums[k] = 0 
#         return nums
# print(moveZeroes([0,1,0,3,12]))