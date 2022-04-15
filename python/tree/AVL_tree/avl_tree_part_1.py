class AVLTree:

    class __Node:
        value = None
        left = None
        right = None

        heightLeft = None
        heightRight = None

        def __init__(self, value, heightLeft, heightRight):
            self.value = value
            self.heightLeft = heightLeft
            self.heightRight = heightRight

        def print(self):
            return "value: {}, left: {}, right: {}, height left: {}, height right {}".\
                format(self.value, 
                    self.left.value if self.left != None else None,
                    self.right.value if self.right != None else None,
                    self.heightLeft,
                    self.heightRight
                )
    
    __root = None

    def insert(self, value):
        """!
        Inserts an element in the tree.
        """

        if self.__root == None:
            self.__root = self.__Node(value, 0, 0)
            return
        
        currentNode = self.__root

        while True: # exit condition

            # we are at a leaf
            if currentNode.value == None:
                currentNode.value = value
                self.__adaptHeight(self.__root)
                return

            # travers to the left
            if value < currentNode.value:
                # is a leaf
                if currentNode.left == None:
                    currentNode.left = self.__Node(None, 0, 0)
                currentNode = currentNode.left
            # travers to the right
            else:
                # is a leaf
                if currentNode.right == None:
                    currentNode.right = self.__Node(None, 0, 0)
                currentNode = currentNode.right

    def __adaptHeight(self, node):
        """!
        Adapts the height of the tree in dft manner. (recursive)
        """
        if node.left == None:
            node.heightLeft = 0
        else:
            node.heightLeft = self.__adaptHeight(node.left)
        
        if node.right == None:
            node.heightRight = 0
        else:
            node.heightRight = self.__adaptHeight(node.right)
        return max(node.heightLeft+1, node.heightRight+1)


    def printBFT(self):
        """!
        Prints the tree in breadth first traversal.
        """
        if self.__root == None:
            print(None)
            return
        
        queue = [self.__root]

        while len(queue) > 0:

            currentNode = queue[0]
            queue = queue[1:]

            print(currentNode.print())

            if currentNode.left != None:
                queue.append(currentNode.left)
            if currentNode.right != None:
                queue.append(currentNode.right)

if __name__ == "__main__":
    tree = AVLTree()
    data = [1, 2, 3, 4, 5, 6]

    for value in data[::-1]:
        tree.insert(value)
    
    tree.printBFT()

