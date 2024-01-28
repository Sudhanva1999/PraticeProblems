class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        startIndex = 0
        zeroCount = 0
        for i,c in enumerate(nums):
            if c == 0:
                zeroCount += 1
            
            while( zeroCount > k):
                if(nums[startIndex] == 0):
                    zeroCount -= 1
                startIndex += 1
            
            maxLen = max(maxLen, (i - startIndex) +1)
        
        return maxLen

        