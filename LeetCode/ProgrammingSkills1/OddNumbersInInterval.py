# Given two non-negative integers low and high. Return 
# the count of odd numbers between low and high (inclusive).
def countOdds(low, high):
    if(low%2 ==0):
        low+=1
    if(high%2 ==0):
        high-=1
    odd = (high-low)//2 +1  
    return odd 
low, high = map(int, input("Enter number range to find number of odd numbers\n").split())
print(countOdds(low, high))