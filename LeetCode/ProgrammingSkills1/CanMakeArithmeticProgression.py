# A sequence of numbers is called an arithmetic progression if the 
# difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be 
# rearranged to form an arithmetic progression. Otherwise, return 
# false.
def canMakeArithmeticProgression(arr):
        arr.sort()
        i = 0 
        flag = 0
        r = arr[1] - arr[0]
        while(i < len(arr)-1):
            if not ((arr[i+1] - arr[i]) == r):
                flag = 1 
            i += 1
        if flag == 1:
            return False
        else:
            return True
print(canMakeArithmeticProgression(list(map(int,input("Enter array to find if it can be rearranged to form Arithmatic Progression\n").split()))))