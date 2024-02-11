class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freqArray = {}
        for i in arr:
            freqArray[i] = freqArray.get(i, 0) + 1

        if(len(freqArray.values()) == len(set(freqArray.values()))):
            return True
        else:
            return False
        