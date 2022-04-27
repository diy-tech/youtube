import numpy as np

arrLen = 10
randMin = 1
randMax = 100

arr = np.random.randint(randMin, randMax, arrLen)

print(arr)

def swap(arr, i, j):
    """!
    Swaps the index i with index j of array arr.
    """
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]

def forwardsRun(arr):
    """!
    Performs a forwards run of shakersort.
    """
    swapped = False
    for i in range(arrLen-1):
        if arr[i] > arr[i+1]:
            swap(arr, i, i+1)
            swapped = True
    return swapped

def backwardsRun(arr):
    """!
    Performs a backwards run of shakersort.
    """
    swapped = False
    for i in range(arrLen-1, 0, -1):
        if arr[i] < arr[i-1]:
            swap(arr, i, i-1)
            swapped = True
    return swapped

swapped = True
forwards = True

while swapped:
    if forwards:
        swapped = forwardsRun(arr)
    else:
        swapped = backwardsRun(arr)
    forwards = not forwards

print(arr)
