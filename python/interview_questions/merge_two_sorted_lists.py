import numpy as np

listA = list(np.random.randint(0, 100, 5))
listA.sort()
print(listA)

listB = list(np.random.randint(0, 100, 5))
listB.sort()
print(listB)

cntA = 0
cntB = 0

result = []

while cntA < len(listA) or \
    cntB < len(listB):

    if cntA >= len(listA):
        result.extend(listB[cntB:])
        cntB = len(listB)
    elif cntB >= len(listB):
        result.extend(listA[cntA:])
        cntA = len(listA)
    elif listA[cntA] <= listB[cntB]:
        result.append(listA[cntA])
        cntA +=1
    else:
        result.append(listB[cntB])
        cntB += 1

print(result)
