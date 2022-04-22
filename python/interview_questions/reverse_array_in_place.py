import math

arr = [*range(13)]

print(arr)

n = len(arr)

for i in range(math.floor(n/2)):
    arr[i] = arr[i] ^ arr[n-i-1]
    arr[n-i-1] = arr[i] ^ arr[n-i-1]
    arr[i] = arr[i] ^ arr[n-i-1]

print(arr)
