# There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
def arraySign(nums):
        prod = 1
        for i in nums:
            prod *= i 
        if (prod == 0):
            return 0
        elif(prod * -1 == abs(prod)):
            return -1 
        else:
            return 1 
print(arraySign(list(map(int,input("Enter an array to find sign of product of its elements.\n").split()))))