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
        trace = []
        while True: # exit condition
            
            trace.append(currentNode)

            # we are at a leaf
            if currentNode.value == None:
                currentNode.value = value
                # adapt height of our trace
                if len(trace) > 2:
                    self.__adaptHeight(trace)

                # checks for imbalance
                node = self.__checkHeight()

                # rotation for weight balancing
                if node != None:
                    self.__rotate(node)

                return

            # travers to the left
            if value < currentNode.value:
                # is a leaf
                if currentNode.left == None:
                    currentNode.left = self.__Node(None, 0, 0)
                    currentNode.heightLeft = 1
                    if currentNode.right != None:
                        trace = []
                currentNode = currentNode.left
            # travers to the right
            else:
                # is a leaf
                if currentNode.right == None:
                    currentNode.right = self.__Node(None, 0, 0)
                    currentNode.heightRight = 1
                    if currentNode.left != None:
                        trace = []
                currentNode = currentNode.right

    def __rotate(self, node):
        """!
        Invokes the balancing method for the tree.
        """
        # node is right heavvy
        if node.heightLeft - node.heightRight < -1:
            # node is right right heavy
            if node.right.heightLeft < node.right.heightRight:
                self.__singleRotationLeft(node)
            # node is right left heavvy
            else:
                self.__doubleRotationRightLeft(node)
        # node is left heavvy
        else:
            # node is left left heavy
            if node.left.heightLeft > node.left.heightRight:
                self.__singleRotationRight(node)
            # node is left right heavvy
            else:
                self.__doubleRotationLeftRight(node)
    
    def __doubleRotationRightLeft(self, node):
        """!
        Performs a right left rotation
        """
        self.__singleRotationRight(node.right)
        self.__singleRotationLeft(node)
    
    def __doubleRotationLeftRight(self, node):
        """!
        Performs a right left rotation
        """
        self.__singleRotationLeft(node.left)
        self.__singleRotationRight(node)

    def __singleRotationLeft(self, node):
        """!
        Performs a single left rotation.
        """
        predecessor = self.__findPredecessor(node)
        tmp = node.right.left
        currentNode = node.right

        if node == self.__root:
            self.__root = currentNode
        else:
            if predecessor.right == node:
                predecessor.right = currentNode
            else:
                predecessor.left = currentNode
        currentNode.left = node
        node.right = tmp

        # OPTIMIZATION POSSIBLE
        self.__adaptHeightAll(self.__root)
    
    def __singleRotationRight(self, node):
        """!
        Performs a single right rotation.
        """
        predecessor = self.__findPredecessor(node)
        tmp = node.left.right
        currentNode = node.left

        if node == self.__root:
            self.__root = currentNode
        else:
            if predecessor.right == node:
                predecessor.right = currentNode
            else:
                predecessor.left = currentNode
        currentNode.right = node
        node.left = tmp

        # OPTIMIZATION POSSIBLE
        self.__adaptHeightAll(self.__root)


    def __findPredecessor(self, node):
        """!
        Return the predecessor of our node.
        """
        return self.__findPredecessorRec(self.__root, node)

    def __findPredecessorRec(self, currentNode, node):

        if currentNode.left == node or \
            currentNode.right == node:
            return currentNode
        else:
            if currentNode.left != None:
                return self.__findPredecessorRec(currentNode.left, node)
            if currentNode.right != None:
                return self.__findPredecessorRec(currentNode.right, node)

    def __checkHeight(self):
        """!
        Checks, if the in the subtree is imbalanced.
        """
        queue = [self.__root]

        while len(queue) > 0:

            currentNode = queue[0]
            queue = queue[1:]
            
            if abs(currentNode.heightLeft - currentNode.heightRight) > 1:
                return currentNode

            if currentNode.right != None:
                queue.insert(0, currentNode.right)
            if currentNode.left != None:
                queue.insert(0, currentNode.left)

        return None

    def __adaptHeight(self, trace):
        """!
        Adapt the height of the nodes in the trace if necessary.
        """
        trace.reverse()
        node = trace[0]
        trace = trace[1:]

        for tmp in trace:
            maxHeight = max(node.heightLeft+1, node.heightRight+1)
            if node == tmp.left:
                tmp.heightLeft = maxHeight
            else:
                tmp.heightRight = maxHeight
            node = tmp

    def __adaptHeightAll(self, node):
        """!
        Adapts the height of the tree in dft manner. (recursive)
        """
        if node.left == None:
            node.heightLeft = 0
        else:
            node.heightLeft = self.__adaptHeightAll(node.left)
        
        if node.right == None:
            node.heightRight = 0
        else:
            node.heightRight = self.__adaptHeightAll(node.right)
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

