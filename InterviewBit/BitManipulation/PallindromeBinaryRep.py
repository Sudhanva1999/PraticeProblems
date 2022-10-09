# Given an integer A find the Ath number whose binary
#  representation is a palindrome.
def reverse(A):
            rev = 0
            while(A):
                lb = A & 1 
                rev = rev | lb 
                rev = rev << 1 
                A = A >> 1 
            rev = rev >> 1 
            return rev 
def solve(A):
        length = 1 
        count = 1
        while(count < A):
            length += 1
            pallNumAtN = 1 << (int((length-1)/2))
            count += pallNumAtN 
            
        count -= (1 << (int((length-1)/2)))
        offset = A - count - 1 
        number = 1 << length - 1 
        offset = offset << (int(length/2))
        number = number | offset
        rev = reverse(number)
        number = number | rev
        return number 
print(solve(int(input("Enter a number n to find nth pallindrom\n"))))

