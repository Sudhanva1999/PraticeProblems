import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        hashMapHave = {}
        hashMapNeed = {}

        for i in t:
            hashMapNeed[i] = 1 + hashMapNeed.get(i, 0)
        
        have = 0
        need = len(hashMapNeed)

        l = 0
        r = 0
        res = [-1, -1]
        minLen = math.inf
        
        for r in range(len(s)):
            c = s[r]
            hashMapHave[c] = 1 + hashMapHave.get(c, 0)
            if(c in hashMapNeed and hashMapHave[c] == hashMapNeed[c]):
                have += 1
            while(have == need):
                if(r-l+1 < minLen):
                    minLen = r-l+1
                    res = [l, r]
                hashMapHave[s[l]] = hashMapHave.get(s[l], 0) - 1
                if(s[l] in hashMapNeed and  hashMapHave[s[l]] < hashMapNeed[s[l]]):
                    have -= 1
                l += 1
            
        l, r = res
        if(minLen != math.inf):
            return s[l:r+1]
        else:
            return ""
        
        