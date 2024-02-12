import math
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start<= end:
            mid = math.floor((start + end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]: start = mid + 1
                else : end = mid -1
            else :
                if target >= nums[start] and target < nums[mid]: end = mid -1
                else : start = mid + 1
        return -1