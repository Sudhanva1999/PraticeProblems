class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        power = 1

        if(n == 1):
            return True
        i = 0
        while(i <= 30):
            power = power * 2 
            if(power == n):
                return True
            i += 1
        
        return False