# Given a string s, find the first non-repeating character 
# in it and return its index. If it does not exist, 
# return -1.

def firstUniqChar(s):
        dic = {}
        
        for c in s:
            dic[c] = not c in dic
            
        for c in s:
            if dic[c]:
                return s.find(c)   
        return -1
print(firstUniqChar("ssfttuvbbv"))