class Selectionsort:

    def __swap(self, data, i, j):
        """!
        Swaps the items at position i and j in the data array.
        Returns a data array containing the swapped items.    
        """
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        
        return data

    def sort(self, data):
        """!
        Expects a data array with numeric items.
        """

        currIdx = 0
        while currIdx < len(data)-1:

            minIdx = currIdx
            for i in range(currIdx + 1, len(data)):

                if data[i] < data[minIdx]:
                    minIdx = i
            data = self.__swap(data, currIdx, minIdx)
            currIdx += 1

        return data

if __name__  == "__main__":
    sorter = Selectionsort()
    data = [5, 99, 12, 17, 42, -5, -6, -5, 1]

    print(sorter.sort(data))