class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getMostFrequent(hashMap):
            mostFrequent = s[0]
            scount = 0
            for key in hashMap:
                if hashMap[key] > scount:
                    scount = hashMap[key]
                    mostFrequent = key
            return scount

        hashMap = {}
        l = 0
        r = 0
        res = 0
        for r in range(0, len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1

            while((r - l + 1) - getMostFrequent(hashMap) > k):
                hashMap[s[l]] = hashMap.get(s[l], 0) - 1
                l += 1
            res = max(res, r-l+1)
        return res