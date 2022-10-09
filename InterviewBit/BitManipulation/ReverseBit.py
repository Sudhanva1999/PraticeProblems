# Reverse the bits of an 32 bit unsigned integer A.
def reverse(A):
    rev = 0 
    i = 0
    while(i < 32):
        rev = rev << 1
        if((A & 1) == 1):
            rev = rev ^ 1
        A = A >> 1
        i += 1
    
    return rev  

print(reverse(int(input("Enter an integer to find decimal form of reversed bits of the integer.\n"))))