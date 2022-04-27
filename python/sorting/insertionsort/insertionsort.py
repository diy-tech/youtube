import numpy as np

arrLen = 10
randMin = 1
randMax = 100

arr = np.random.randint(randMin, randMax, arrLen)

print(arr)

result = np.full(arrLen, randMin)

print(result)

for i in range(arrLen):
    j = i

    while j > 0:
        if result[j-1] < arr[i]:
            break
        result[j] = result[j-1]
        j -= 1

    result[j] = arr[i]

print(result)
