class MAryTree:

    class __Node:
        children = []
        value = None

        def __init__(self, value, m):
            self.value = value
            self.children = [None]*m

    m = None
    __root = None

    def __init__(self, m):
        self.m = m

    def insert(self, value):
        """!
        Inserts a node in bft order.
        """

        if self.__root == None:
            self.__root = self.__Node(value, self.m)
            return
        
        queue = [self.__root]

        inserted = False
        while not inserted: 

            node = queue[0]
            queue = queue[1:]

            for i in range(self.m):
                if node.children[i] == None:
                    node.children[i] = self.__Node(value, self.m)
                    inserted = True
                    break
                else:
                    queue.append(node.children[i])
    
    def print(self):
        """!
        Prints the tree in bft order.
        """
        if self.__root == None:
            print(None)
            return
        
        queue = [self.__root]

        while len(queue) > 0:

            node = queue[0]
            queue = queue[1:]

            for i in range(self.m):
                if node.children[i] != None:
                    queue.append(node.children[i])
            print(node.value)

if __name__ == "__main__":
    mTree = MAryTree(3)

    for i in range(1, 13):
        mTree.insert(i)
    
    mTree.print()
