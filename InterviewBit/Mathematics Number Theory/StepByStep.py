# Given a target A on an infinite number line, i.e. -infinity to
#  +infinity.You are currently at position 0 and you need to reach 
#  the target by moving according to the below rule:
# In ith move you can take i steps forward or backward.
# Find the minimum number of moves required to reach the target.
import math
def solve(A):
        A = abs(A)
        
        last = int((math.sqrt(1+(8*A))-1)//2)
        running_sum = (last*(last+1))//2
        
        while (running_sum < A) or (running_sum - A) % 2 != 0:
            last += 1
            running_sum += last
        return last
print(solve(int(input("Enter a number to find steps needed to reach it.\n"))))