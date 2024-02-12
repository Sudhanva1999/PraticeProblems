import math
class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        e = x - 1
        tempAns = -1
        if(x == 0 or x == 1):
            return x
        while(s <= e):
            mid = math.floor((s+e)/2)
            if((mid*mid) == x):
                return mid
            elif((mid*mid) > x):
                e = mid - 1
            else:
                tempAns = mid
                s = mid + 1
        return tempAns
            