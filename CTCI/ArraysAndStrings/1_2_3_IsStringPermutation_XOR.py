# Given 2 strings determine if one is permutation 
# of other

string1 = input("Enter 1st String\n")
string2 = input("Enter 2nd String\n")

res = 0

for c in string1:
    res = res ^ ord(c)
for c in string2:
    res = res ^ ord(c) 

if res != 0:
     print("Strings are not permutation")
else:
     print("Strings are permutation")