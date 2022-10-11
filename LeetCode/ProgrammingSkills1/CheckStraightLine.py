# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
# represents the coordinate of a point. Check if these points make a straight
#  line in the XY plane.

def checkStraightLine(coordinates):
        if(len(coordinates) < 3):
            return True
        if((coordinates[2][0] - coordinates[1][0]) == 0):
            flag = 0
            ref = coordinates[2][0]
            for i in coordinates:
                if(i[0]!= ref):
                    flag = 1 
            if flag == 1:
                return False
            else:
                return True
        elif((coordinates[2][1] - coordinates[1][1]) == 0):
            flag = 0
            ref = coordinates[2][1]
            for i in coordinates:
                if(i[1]!= ref):
                    flag = 1 
            if flag == 1:
                return False
            else:
                return True
        else:
            m = (coordinates[2][1] - coordinates[1][1]) / (coordinates[2][0] - coordinates[1][0])
            c = coordinates[1][1] - (m*coordinates[1][0])
            flag = 0
            for i in coordinates:
                if(i[1] != (m*i[0])+c):
                    flag = 1 
            if(flag == 1):
                return False
            else:
                return True

print(checkStraightLine([[0,0],[0,1]]))