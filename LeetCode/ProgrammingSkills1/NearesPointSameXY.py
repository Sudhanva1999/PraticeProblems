# You are given two integers, x and y, which represent your current
# location on a Cartesian grid: (x, y). You are also given an array
# points where each points[i] = [ai, bi] represents that a point 
# exists at (ai, bi). A point is valid if it shares the same
# x-coordinate or the same y-coordinate as your location.
# Return the index (0-indexed) of the valid point with the smallest 
# Manhattan distance from your current location. If there are multiple,
# return the valid point with the smallest index. If there are no
# valid points, return -1.
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
def nearestValidPoint(x, y, points):
        indexMin = 999999999
        min = 999999999
        flag = 0
        for index,point in enumerate(points):
            if(point[0] == x or point[1] == y):
                distance = abs(point[0]-x) + abs(point[1]-y)
                if(distance < min):
                    indexMin = index 
                    min = distance
                flag = 1
        if (flag == 0):
            return -1     
        return indexMin 
print(nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))