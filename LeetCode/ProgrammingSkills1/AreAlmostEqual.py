# You are given two strings s1 and s2 of equal length. A string swap
# is an operation where you choose two indices in a string 
# (not necessarily different) and swap the characters at these 
# indices.
# Return true if it is possible to make both strings equal by 
# performing at most one string swap on exactly one of the strings.
#  Otherwise, return false.
def areAlmostEqual(s1,s2):
        if (s1 == s2):
            return True
        if(len(s1) != len(s2)):
            return False 
        difCount = 0 
        i = 0 
        ind = []
        while(i < len(s1)):
            if(s1[i] != s2[i]):
                difCount += 1 
                ind.append(i)
            i += 1
        if (difCount != 2):
            return False
        temp = s1[ind[0]]
        s1new1 = s1[:ind[0]] + s1[ind[1]] + s1[ind[0] + 1:]
        s1new2 = s1new1[:ind[1]] + s1[ind[0]] +s1new1[ind[1] + 1:]
        if(s1new2 == s2):
            return True
        else:
            return False 
inpStrings = input("Enter strings to find if they can be made equal with one swap.\n").split(" ")
print(areAlmostEqual(inpStrings[0],inpStrings[1]))