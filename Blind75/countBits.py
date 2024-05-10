def countBits(n):
        prevList = [0] * (n + 1)
        offset = 1 
        currPower = 2
        if(n == 0):
            return [0]
        
        for i in range(1, n+1):
            if(i == currPower):
                currPower *= 2
                offset *= 2
            
            prevList[i] = 1 + prevList[i - offset]
        
        return prevList

print(countBits(2))