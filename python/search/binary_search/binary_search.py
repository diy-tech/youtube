import math

class BinarySearch:

    def searchIterative(self, data, searchValue):
        """!
        data has to be an array that sorted ascending and 
        has numeric values. 
        searchValue is the value to search for in data.
        Returns the index of searchValue in data or None
        if it was not found.
        """

        left = 0
        right = len(data)-1
        
        while left <= right: # exit condition for loop

            index = left + math.ceil((right-left)/2)

            # search value found
            if data[index] == searchValue:
                return index
            # look on the left side
            elif searchValue < data[index]:
                right = index-1
            # look on the right side 
            else:
                left = index+1
        return None

    def searchRecursive(self, data, searchValue):
        return self.__searchRec(data, searchValue, 0, len(data)-1)

    def __searchRec(self, data, searchValue, left, right):

        if left > right:
            return None

        index = left + math.ceil((right-left)/2)

        # value found        
        if searchValue == data[index]:
            return index
        # look left
        elif searchValue < data[index]:
            return self.__searchRec(data, searchValue, left, index-1)
        # look right
        else:
            return self.__searchRec(data, searchValue, index+1, right)

if __name__ == "__main__":

    binSearch = BinarySearch()

    data = [1, 2, 4, 6, 7, 9]

    for i in data:
        print(binSearch.searchRecursive(data, i))

    print(binSearch.searchRecursive(data, -1))
    print(binSearch.searchRecursive(data, 10))
    print(binSearch.searchRecursive(data, 3))
