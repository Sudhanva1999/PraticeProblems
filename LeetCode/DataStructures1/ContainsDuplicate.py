# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element 
# is distinct.
def containsDuplicate(nums):
    nums.sort()
    i=0
    while(i<(len(nums)-1)):
        if(nums[i]==nums[i+1]):
            return True
        i+=1
    return False 
print(containsDuplicate(list(map(int,input("Enter an array to find if its a set.\n").split()))))