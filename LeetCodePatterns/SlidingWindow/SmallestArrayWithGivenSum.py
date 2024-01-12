class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0 
        minLength = len(nums)
        startIndex = 0
        noarray = True
        for i, num in enumerate(nums):
            currentSum = currentSum + num
            while(currentSum >= target):
                curLength = (i - startIndex )+1
                minLength = min(minLength, curLength)
                noarray = False
                currentSum -= nums[startIndex]
                startIndex += 1        
        if noarray:
            return 0
        else:
            return minLength



        



        