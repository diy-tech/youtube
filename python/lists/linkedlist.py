class LinkedList:

    class ListItem:
        value = None
        next = None
    
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

    l.print()

    l.add(1)
    l.add(2)
    l.add(3)

    l.print()

    l.delete(2)
    l.print()

    l.delete(1)
    l.print()

    l.delete(3)
    l.print()