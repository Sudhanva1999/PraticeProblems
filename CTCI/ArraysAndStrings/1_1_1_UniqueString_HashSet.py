# Time:O(n)
# Space:O(1)
problemString = input("Enter the string to find if all characters are unique\n")
mapStore = {}
flag = 1
if(len(problemString) > 128):
    flag = 0
else:
    for c in problemString:
        if c in mapStore.keys():
            flag = 0  
        else: 
            mapStore[c] = 1

if(flag == 0):
    print("Not all chars Unique")
else:
    print("All chars unique")