class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(mid,position,m):
            lastPos = 0
            cowCount = 1


            for i, pos in enumerate(position):
                if(pos - position[lastPos] >= mid):
                    cowCount += 1
                    if(cowCount >= m):
                        return True
                    lastPos = i

            return False
    
        sorted_p = sorted(position)

        s = 0
        e = sorted_p[-1] - sorted_p[0]
        ans = -1
        while(s <= e):
            mid = math.floor((s+e)/2)
            if(isPossible(mid, sorted_p, m)):
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
                
        return ans