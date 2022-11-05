# Given an integer numRows, return the first numRows 
# of Pascal's triangle.
# In Pascal's triangle, each number is the sum of 
# the two numbers directly above it as shown:

def generate(numRows):
        if(numRows == 1):
            return [[1]]
        if(numRows == 2):
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for i in range(2, numRows):
            prevRow = result[i-1]
            curRow = [1]
            for k in range(0, i-1):
                curRow.append(prevRow[k]+prevRow[k+1])
            curRow.append(1)
            result.append(curRow)
        return result 
print(generate(4))