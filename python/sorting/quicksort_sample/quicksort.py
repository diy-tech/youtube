import random

class Quicksort:

    def sort(self, data):
        """!
        Data is a array of numeric items.
        """

        if len(data) <= 1:
            return data

        left = []
        right = []
        pivot = random.randint(0, len(data)-1)

        for i in range(len(data)):

            if i == pivot:
                continue
            elif data[i] <= data[pivot]:
                left.append(data[i])
            else:
                right.append(data[i])
        
        result = []

        result.extend(self.sort(left))
        result.append(data[pivot])
        result.extend(self.sort(right))

        return result

if __name__ == "__main__":

    sorter = Quicksort()
    data = [-1, 99, 88, 42, 71, 17 ,24, 23, 23, -6, -7]

    print(sorter.sort(data))
