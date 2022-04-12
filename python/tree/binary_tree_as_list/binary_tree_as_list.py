class BinaryTreeAsList:

    class __Node:
        left = None
        right = None
        value = None

        def __init__(self, value):
            self.value = value

    __root = None

    def insertIterative(self, value):
        """!
        Inserts an element into the tree.
        value is the value of the node.
        """
        # node is root node
        if self.__root == None:
            self.__root = self.__Node(value)
        else:

            queue = [self.__root]

            while len(queue) > 0:
                
                node = queue[0]

                # left node is leaf
                if node.left == None:
                    node.left = self.__Node(value)
                    return
                # right node is leaf
                elif node.right == None:
                    node.right = self.__Node(value)
                    return
                # no leaf at current node
                else:
                    queue.extend([node.left, node.right])
                
                queue = queue[1:]

    def printBFS(self):

        if self.__root == None:
            print(None)
        else:
            queue = [self.__root]

            while len(queue) > 0:
                node = queue[0]

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                
                print(node.value)
                queue = queue[1:]

    
    def insertRecursive(self, value):
        """!
        Inserts value into the tree in recursive and breadth first fashion.
        """
        if self.__root == None:
            self.__root = self.__Node(value)
        else:
            self.__insertRec(value, [self.__root])
        
    def __insertRec(self, value, toDo):

        node = toDo[0]

        # left is leaf
        if node.left == None:
            node.left = self.__Node(value)
        # right is leaf
        elif node.right == None:
            node.right = self.__Node(value)
        else:
            if node.left != None:
                toDo.append(node.left)
            if node.right != None:
                toDo.append(node.right)
            toDo = toDo[1:]
            self.__insertRec(value, toDo)

if __name__ == "__main__":

    binTree = BinaryTreeAsList()
    data = [1, 2, 3, 4, 5, 6, 7]

    for elem in data:
        binTree.insertRecursive(elem)

    binTree.printBFS()