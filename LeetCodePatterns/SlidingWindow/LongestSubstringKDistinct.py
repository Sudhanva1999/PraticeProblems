def kDistinctChars(k, str):
    hashstore = {}
    maxLen = 0
    startIndex = 0
    for i,c in enumerate(str):
        hashstore[c] = hashstore.get(c, 0) + 1
        maxLen += 1
        if len(hashstore) > k:
            hashstore[str[startIndex]] -= 1
            if hashstore[str[startIndex]] == 0:
                del hashstore[str[startIndex]]
            startIndex += 1
            maxLen -= 1
    if len(hashstore) == 1:
        return list(hashstore.values())[0]
     
    return maxLen


