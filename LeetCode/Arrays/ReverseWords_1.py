class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = list(filter(lambda a: a != "", s))
        
        i = 0 
        j = len(s) - 1
        while (i < len(s)//2):
            s[j],s[i] = s[i],s[j]
            i += 1
            j -= 1 
        return " ".join(s).strip()
        