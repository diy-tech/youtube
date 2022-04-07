class Bubblesort:

    def __swap(self, data, i, j):
        """!
        Swaps the two items at position i and j in data.
        Returns a new list.
        """
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        
        return data

    def sort(self, data):
        """! 
        Expects a list of numbers as an input.
        """
        n = len(data)

        # runs
        while n > 1:
            didSwap = False
            # swaps
            for i in range(n-1):
                if data[i] > data[i+1]:
                    data = self.__swap(data, i, i+1)
                    didSwap = True
            if didSwap:
                n -= 1
            else:
                break
        return data

if __name__ == "__main__":
    sorter = Bubblesort()
    data = [42, 13, 55, 34, 1]

    print(sorter.sort(data))
    print(range(10))
