class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hMapS = {}
        hMapT = {}
        for i in range(0, len(s)):
            hMapS[s[i]] = hMapS.get(s[i], 0) + 1
            hMapT[t[i]] = hMapT.get(t[i], 0) + 1
        
        for c in hMapS:
            if hMapS[c] != hMapT.get(c, 0):
                return False
        
        return True