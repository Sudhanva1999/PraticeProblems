# Given 2 strings determine if one is permutation 
# of other

string1 = input("Enter 1st String\n")
string2 = input("Enter 2nd String\n")
res1 = ''.join(sorted(string1))
res2 = ''.join(sorted(string2))

if(res1 != res2):
    print("Strings are not permutation")
else:
    print("Strings are permutation")