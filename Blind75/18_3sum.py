class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if(num == nums[i - 1] and i!=0):
                continue
            l = i + 1
            r = len(nums) - 1 

            while l < r: 
                threeSum = nums[l] + nums[r] + num
                if(threeSum > 0):
                    r -= 1
                elif(threeSum < 0):
                    l += 1
                else:
                    res.append([num,nums[l], nums[r]])
                    l += 1 
                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
        return res
