k = 1 
str = "abcabcbb"
hashstore = {}
maxLen = 0
startIndex = 0
for i,c in enumerate(str):
    hashstore[c] = hashstore.get(c, 0) + 1
    maxLen += 1
    if hashstore[c] > k:
        hashstore[str[startIndex]] -= 1
        if hashstore[str[startIndex]] == 0:
            del hashstore[str[startIndex]]
        startIndex += 1
        maxLen -= 1
    if len(hashstore) == 1:
        print(list(hashstore.values())[0])
     
print(maxLen)