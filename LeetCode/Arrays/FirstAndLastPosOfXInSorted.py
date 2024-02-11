import math
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getLeftPos(nums, key):        
            s = 0
            e = len(nums)-1
            lmost = -1 
            mid = math.floor((s + e)/2)
            while(s <= e):
                if nums[mid] == key:
                    lmost = mid 
                    e = mid - 1
                elif nums[mid] < key:
                    s = mid + 1
                else:
                    e = mid - 1 
                mid = math.floor((s + e)/2)
            return lmost 
        def getRightPos(nums, key):
            s = 0
            e = len(nums)-1
            rmost = -1 
            mid = math.floor((s + e)/2)
            while(s <= e):
                if nums[mid] == key:
                    rmost = mid 
                    s = mid + 1
                elif nums[mid] < key:
                    s = mid + 1
                else:
                    e = mid - 1 
                mid = math.floor((s + e)/2)
            return rmost 

        return [getLeftPos(nums, target), getRightPos(nums, target)]
   