class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashstore = {}
        startIndex = 0
        maxLen = 0
        for i,c in enumerate(s):
            if(c in hashstore.keys() and startIndex <= hashstore[c]):
                startIndex = hashstore[c] + 1
                hashstore[c] = i
            else:
                hashstore[c] = i
            maxLen = max(maxLen, (i - startIndex) + 1)
        return maxLen

        