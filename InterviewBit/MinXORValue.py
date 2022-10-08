# Given an integer array A of N integers, find the pair of integers in 
# the array which have minimum XOR value. Report the minimum XOR value.

def findMinXor(A):
        A.sort()
        min = 9999999999
        i = 0 
        while(i < len(A)-1):
            if((A[i]^A[i+1]) < min):
                min = (A[i]^A[i+1])
            i += 1 
        return min 

A = list(map(int,input("Enter an Array to find min XOR pair.\n").split()))
print (findMinXor(A))