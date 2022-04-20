class LinkedList:

    class ListItem:
        value = None
        next = None

        def __init__(self, value=None):
            self.value = value
    
    anchor = ListItem()

    def add(self, value):
        """!
        Appends a new element at the end of the list.
        """

        node = self.ListItem()
        node.value = value

        if self.anchor.next == None:
            self.anchor.next = node
        else:
            tmpNode = self.anchor.next

            while tmpNode.next != None:
                tmpNode = tmpNode.next
            tmpNode.next = node
    
    def addNode(self, node):
        """!
        Appends a node into the list.
        """
        if self.anchor.next == None:
            self.anchor.next = node
        else:
            tmpNode = self.anchor.next

            while tmpNode.next != None:
                tmpNode = tmpNode.next
            tmpNode.next = node

            if self.isCycle():
                tmpNode.next = None
                return False
        return True

    def isCycle(self):
        """!
        Detects a cycle in the linked list.
        Returns True if a cycle exists, otherwise False
        """
        tmpNode = self.anchor.next

        nodesInList = set()

        while tmpNode != None:
            if tmpNode in nodesInList:
                return True
            else:
                nodesInList.add(tmpNode)
                tmpNode = tmpNode.next
    
        return False

    def delete(self, value):
        """!
        Delete the first occurence of the value in the list.
        """
        tmpNode = self.anchor

        while tmpNode.next != None:

            if tmpNode.next.value == value:
                # delete tmpNode.next
                helperNode = tmpNode.next.next
                del tmpNode.next
                tmpNode.next = helperNode
                break
            else:
                tmpNode = tmpNode.next


    def print(self):
        """!
        Prints the whole list.
        """
        tmpNode = self.anchor.next

        if tmpNode == None:
            print(None)

        while tmpNode != None:
            print(tmpNode.value)
            tmpNode = tmpNode.next

if __name__ == "__main__":

    l = LinkedList()

    node1 = LinkedList.ListItem(1)
    node2 = LinkedList.ListItem(2)
    node3 = LinkedList.ListItem(3)

    print(l.addNode(node1))
    print(l.addNode(node2))
    print(l.addNode(node3))
    print(l.addNode(node1))

    l.print()

    