class BinarySearchTree:

    class __Node:
        left = None
        right = None
        value = None

        def __init__(self, value):
            self.value = value

    __root = None

    def insert(self, value):
        """!
        Inserts a value into the binary search tree.
        """
        if self.__root == None:
            self.__root = self.__Node(value)
            return
        
        currentNode = self.__root
        # traversal until we found the appropriate node
        while currentNode.value != None:
            # travers to the left
            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = self.__Node(None)
                currentNode = currentNode.left
            # travers to the right
            else:
                if currentNode.right == None:
                    currentNode.right = self.__Node(None)
                currentNode = currentNode.right

        # node is leaf
        if currentNode.value == None:
            currentNode.value = value

    def printBFT(self):
        """!
        Prints the tree in breadth first traversal (bft) order.
        """

        if self.__root == None:
            print(None)
            return
        
        queue = [self.__root]

        while len(queue) > 0:

            node = queue[0]
            queue = queue[1:]

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            
            print(node.value)
    
if __name__ == "__main__":

    bst = BinarySearchTree()
    data = [5, 8, 6, 9, 12, 4, 1, 3]

    for value in data:
        bst.insert(value)

    bst.printBFT()

