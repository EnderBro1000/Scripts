thingThatGoesIn = "754388489999793138912431545258"

def longest_substring():
    
    currentCount = 0
    bestPos = 0
    bestLen = 0
    pos = 0
    oldChar = int(thingThatGoesIn[0]) + 1
    
    for char in thingThatGoesIn: 
        char = int(char)
        if (char + oldChar) % 2 == 1:
            currentCount += 1
        else:
            if(bestLen < currentCount): 
                bestPos = pos - currentCount
                bestLen = currentCount 
            currentCount = 1
        oldChar = char
        pos += 1
        
    if(bestLen < currentCount): #if it works it works #coding is an art form and my passion
        bestPos = pos - currentCount
        bestLen = currentCount
    
    print(bestPos, bestLen)
    print(thingThatGoesIn[bestPos:bestPos + bestLen])

longest_substring()

