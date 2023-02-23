# Given 2 strings determine if one is permutation 
# of other
# Time: O(n)
# Space: O(1)
string1 = input("Enter 1st String\n")
string2 = input("Enter 2nd String\n")
flag = 0

countHash = {}

if len(string1) != len(string2):
    flag = 1 
else:
    for c in string1:
        if c in countHash.keys():
            countHash[c] = countHash[c] + 1
        else:
            countHash[c] = 1 
        
    for c in string2:
        if c in countHash.keys():
            countHash[c] = countHash[c] - 1 
            if countHash[c] < 0:
                flag = 1 
        else:
            flag = 1

if(flag == 0):
    print("Strings are permutation")
else:
    print("Strings are not permutation")

