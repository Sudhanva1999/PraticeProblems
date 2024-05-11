def missingNumber(nums):
        res = 0
        for i in range(0, len(nums)+ 1):
            res ^= i
        
        for i in nums:
            res ^= i
        return res

print(missingNumber([3,0,1]))