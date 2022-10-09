# Given an integer A, count and return the number of trailing zeroes.
def solve(A):
        count = 0 
        flag = 0 
        while(flag == 0):
            if((A & 1) == 0):
                count += 1
                A = A >> 1
            else:
                flag = 1 
        return count 
print(solve(int(input("Enter a integer to find number of trailing zeros it has in binary form\n"))))