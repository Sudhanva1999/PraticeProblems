class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashstore = {"" : 0}
        maxRepC = ""
        maxRep = 0
        maxLen = 0
        startIndex = 0
        for i,c in enumerate(s):
            hashstore[c] = hashstore.get(c, 0) + 1
            maxRep = max(maxRep, hashstore[c])
            if (((i - startIndex) + 1) - maxRep > k):
                hashstore[s[startIndex]] -= 1
                startIndex += 1 
            maxLen = max(maxLen, (i - startIndex) + 1)
        return maxLen