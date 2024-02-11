import math
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr) - 1
        mid = math.floor((s+e)/2)
        while(s <= e):
            if (arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]):
                return(mid)
            elif(arr[mid] < arr[mid+1]):
                s = mid + 1 
            elif (arr[mid] > arr[mid+1]):
                e = mid - 1
            mid = math.floor((s+e)/2)
        