class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShort = 0xffffffff 

        while b & bitShort != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & bitShort if b > 0 else a