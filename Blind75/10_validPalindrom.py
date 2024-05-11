import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            if( (ord(c) >= ord('a') and ord(c) <= ord('z')) or
                (ord(c) >= ord('A') and ord(c) <= ord('Z')) or
                (ord(c) >= ord('0') and ord(c) <= ord('9'))
            ):
                return True
            else: 
                return False
        l = 0 
        r = len(s) - 1
        while(l < r):
            while(not isAlphaNum(s[l]) and l < len(s) - 1):
                    l += 1
            while(not isAlphaNum(s[r]) and r >= 1):
                    r -= 1
            if((l <=r ) and s[l].lower() == s[r].lower()):
                l += 1
                r -= 1
                continue
            elif(l > r):
                 return True
            else:
                return False
        return True






        