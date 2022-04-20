from textwrap import fill
import numpy as np

class HashSet:

    arr = None
    __size = None

    def __init__(self, __size=10):
        self.__size = __size
        self.arr = np.full(shape=[self.__size], fill_value=None)

    def add(self, value):
        """!
        Adds an item to the hashset.
        """
        index = hash(value)%self.__size
        self.arr[index] = value
    
    def print(self):
        print(self.arr)

if __name__ == "__main__":
    mySet = HashSet(100)

    mySet.add(1)
    mySet.add(2)
    mySet.add(3)
    mySet.add(1123345)
    mySet.add(30)
    mySet.add(40)

    mySet.print()
