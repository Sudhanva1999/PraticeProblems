class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0 
        l = 0
        w = len(height) - 1
        r = w

        while(l < r):
            water = min(height[l], height[r]) * w
            maxWater = max(water, maxWater)

            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
            
            w -= 1

        return maxWater
