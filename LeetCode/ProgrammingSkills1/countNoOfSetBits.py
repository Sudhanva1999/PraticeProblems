# Write a function that takes an unsigned integer and
#  returns the number of '1' bits it has (also known as
#   the Hamming weight).
def hammingWeight(n):
    count = 0 
    while(n):
        if((n & 1) == 1):
            count += 1 
        n = n >> 1
    return count 
print(hammingWeight(int(input("Enter a number to find no of set bits in its binary representation\n"))))
