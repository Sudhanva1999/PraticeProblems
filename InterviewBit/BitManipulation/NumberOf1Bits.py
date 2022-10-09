# Find number of set bits in binary form of an integer. 
def numSetBits(A):
    count = 0 
    while(A != 0):
        A = A & (A-1)
        count += 1 
    return count 

print(numSetBits(int(input("Enter an Integer to find number of set bits it has.\n"))))
