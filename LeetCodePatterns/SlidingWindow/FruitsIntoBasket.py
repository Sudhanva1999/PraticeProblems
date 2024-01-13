class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        hashstore = {}
        maxLen = 0
        startIndex = 0
        for i,c in enumerate(fruits):
            hashstore[c] = hashstore.get(c, 0) + 1
            maxLen += 1
            if len(hashstore) > k:
                hashstore[fruits[startIndex]] -= 1
                if hashstore[fruits[startIndex]] == 0:
                    del hashstore[fruits[startIndex]]
                startIndex += 1
                maxLen -= 1
        if len(hashstore) == 1:
            return list(hashstore.values())[0]
        
        return maxLen
            