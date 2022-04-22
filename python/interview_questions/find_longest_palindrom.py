import math

inputString = "aaaaaaa"

currentLen = len(inputString)

def isPalindrom(inputString):
    n = len(inputString)
    for i in range(math.floor(n/2)-1):
        if inputString[i] != inputString[n-1-i]:
            return False
    return True

longestPalindrom = ""

while currentLen > 0:

    for i in range(len(inputString) - currentLen+1):        
        if isPalindrom(inputString[i:currentLen+i]):
            longestPalindrom = inputString[i:currentLen+i]
            break
    
    if len(longestPalindrom) > 0:
        break
    else:
        currentLen -= 1

print(longestPalindrom)
