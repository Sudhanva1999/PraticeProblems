# Given string find if all chars are unique.
# Time:O(n) / O(1) for fixed char set
# Space:O(1)
problemString = input("Enter the string to find if all characters are unique\n")
blank = 0
flag = 1
if(len(problemString) > 128):
    flag = 0
else:
    for i in problemString:
        x = 1 
        x = x << ord(i) - 97
        if(x & blank):
            flag = 0
        else:
            blank = blank | x 
        
if(flag == 0):
    print("Not all chars Unique")
else:
    print("All chars unique")
