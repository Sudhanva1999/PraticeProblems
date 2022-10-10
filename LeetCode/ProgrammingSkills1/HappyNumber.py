# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the 
# sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
#  or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
def isHappy(n):
        if n == 1:
            return True
        stack = [] 
        while n not in stack:
            stack.append(n)
            sumSq = 0
            temp = n
            while(temp):
                sumSq += (temp % 10) ** 2
                temp //= 10
            n = sumSq 
            if sumSq == 1:
                return True
        return False
print(isHappy(int(input("Enter a number to find if its a Happy Number or not.\n"))))        