# Write a function that reverses a string. The input string is 
# given as an array of characters s.
# You must do this by modifying the input array in-place
#  with O(1) extra memory.

def reverseString(s):
        n = len(s)
        stop = n // 2 - 1
        for i, element in enumerate(s):
            lastIndex = n - (i + 1)
            temp = s[i]
            s[i] = s[lastIndex]
            s[lastIndex] = temp 
            if(i == stop):
                break
        return s
print(reverseString(['a','e','i','o','u']))
