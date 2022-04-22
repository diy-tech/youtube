import random

l = 100

# generate and shuffle the array
arr = [*range(1, l+1)]
random.shuffle(arr)

missingIndex = random.randint(0, l-1)

print("missing index: {}, missing number: {}".format(missingIndex, arr[missingIndex]))

arr[missingIndex] = 0

gSum = l*(l+1)/2

arrSum = 0
for i in range(l):
    arrSum += arr[i]

missingNumber = gSum - arrSum

print("missing number: {}".format(missingNumber))


