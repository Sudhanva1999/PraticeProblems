def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
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
