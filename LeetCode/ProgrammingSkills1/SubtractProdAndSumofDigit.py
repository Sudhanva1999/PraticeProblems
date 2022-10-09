# Given an integer number n, return the difference 
# between the product of its digits
#  and the sum of its digits.
def subtractProductAndSum(n):
    prodDig = 1 
    sumDig = 0
    while(n):
        temp = n % 10 
        prodDig = int(prodDig * temp) 
        sumDig += temp 
        n = n // 10 
    return prodDig - sumDig
print(subtractProductAndSum(int(input("Enter a number to find difference of product and sum of its digits\n"))))