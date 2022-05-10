import numpy as np

# items are 0, 1, 2
values = [1, 7, 15]
weights = [1, 5, 9]

maxWeight = 17

result = np.zeros((len(values)+1, maxWeight+1))

for item in range(1, len(values)+1):
    for weight in range(1, maxWeight+1):
        # fits the item
        if weights[item-1] <= weight:
            result[item][weight] = max(\
                result[item-1][weight],  # previous solution
                values[item-1] + result[item][weight-weights[item-1]]  # construct the new solution
                )
        else:
            result[item][weight] = result[item-1][weight]

print(result)
print("Maximum value for weight {}: {}".format(maxWeight, result[len(values)][maxWeight]))

