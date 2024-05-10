def reverseBits(n):
        rev = 0
        for i in range(0,32):
            rev = rev << 1 
            if((n & 1) == 1):
                rev = rev ^ 1
            n = n >> 1 
        return rev 

print(reverseBits(11111111111111111111111111111101))