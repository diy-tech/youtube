import math

class Mergesort:

    def mergeSort(self, data):
        """!
        Expects a numeric data array as input.
        """
        if len(data) <= 1:
            return data

        left = data[0:math.floor(len(data)/2)]
        right = data[math.floor(len(data)/2):]

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        return self.merge(left, right)

    def merge(self, left, right):
        """!
        Merges the left and right data array.
        """
        result = []
        lenLeft = len(left)
        lenRight = len(right)

        # counter for index in left list
        cntLeft = 0
        # counter for index in right list
        cntRight = 0

        while cntLeft < lenLeft or cntRight < lenRight:
            # left list is empty
            if cntLeft >= lenLeft:
                # extend result by elements left in right list
                result.extend(right[cntRight:])
                break
            # right list is empty
            elif cntRight >= lenRight:
                # extend result by elements left in right list
                result.extend(left[cntLeft:])            
                break
            elif left[cntLeft] <= right[cntRight]:
                result.append(left[cntLeft])
                cntLeft += 1
            else:
                result.append(right[cntRight])
                cntRight += 1

        return result

if __name__ == "__main__":
    sorter = Mergesort()
    data = [2, 1,99, 42, -5, -7, 213]

    print(sorter.mergeSort(data))

    print(data[0:math.floor(len(data)/2)])


