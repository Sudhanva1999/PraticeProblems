# Given an integer array nums, return the largest perimeter 
# of a triangle with a non-zero area, formed from three of 
# these lengths. If it is impossible to form any triangle of
#  a non-zero area, return 0.
def largestPerimeter(nums):
        if(len(nums) < 3):
            return 0 
        nums.sort()
        i = len(nums) - 1
        while(i >= 2):
            if(nums[i] < nums[i-1]+nums[i-2]):
                return nums[i]+nums[i-1]+nums[i-2]
            i -= 1
        return 0 
print(largestPerimeter(list(map(int,input("Enter array to find the largest possible permiter of a triangle\n").split()))))