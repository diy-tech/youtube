class BinaryTreeAsArray:

    tree = None

    def bft(self):
        """!
        Breadth first traversal (bft) of the tree.
        Returns an array of the tree in bft order.
        """
        return self.tree

    def dft(self):
        """!
        Depth first traversal (dft) of the tree.
        Returns an array of the tree in dft order.
        """
        if self.tree == None or \
            len(self.tree) < 1:
            return None
        queue = [0]
        result = []

        # until queue is empty
        while len(queue) > 0:

            index = queue[0]
            # we work on the node and remove therefore
            queue = queue[1:]

            # add children to queue if exist
            for child in [1, 2]:
                if 2*index+child < len(self.tree):
                    queue.insert(0, 2*index+child)
            result.insert(0, index)

        return result

if __name__ == "__main__":
    binTree = BinaryTreeAsArray()
    data = [1, 2, 3, 4, 5, 6, 7]

    binTree.tree = data

    result = binTree.dft()
    print(result)

    for i in range(len(data)):
        print(data[result[i]])
