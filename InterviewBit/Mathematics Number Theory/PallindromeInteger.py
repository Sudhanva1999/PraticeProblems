# Determine whether an integer is a palindrome. Do this without extra
#  space.A palindrome integer is an integer x for which
#   reverse(x) = x where reverse(x) is x with its digit reversed.
#    Negative numbers are not palindromic.
def isPalindrome(A):
        A = str(A)
        if(len(A) == 1):
            return 1
        if(A == A[::-1]):
            return 1
        else:
            return 0
print(isPalindrome(int(input("Enter a number to find if its a pallindrome.\n"))))