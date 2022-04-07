class List:
    
    anchor = None
    last = None
    cnt = -1

    class ListItem:
        value = None
        next = None

        def __init__(self, value) :
            self.value = value

    def add(self, value):
        item = self.ListItem(value)

        if not self.anchor:
            self.anchor = item
            self.last = item
        else:
            self.last.next = item
            self.last = item

        self.cnt += 1

    def print(self):
        tmp = self.anchor

        if self.anchor == None:
            print("List is empty")

        while tmp != None:
            print(tmp.value)
            tmp = tmp.next

    def deleteAt(self, position):
        ctr = 0
        tmp = self.anchor

        if position > self.cnt:
            return
        elif position == 0:
            del self.anchor
            del self.last
        else:

            while ctr < position-1:
                tmp = tmp.next
                ctr += 1      

            if tmp.next == self.last:
                self.last = tmp
                self.last.next = None
                tmp = tmp.next
                del tmp
            else:
                delItem = tmp.next
                tmp.next = tmp.next.next
                del delItem
        self.cnt -= 1

list = List()

list.add(1)
list.add(2)
list.add(3)
list.print()

list.deleteAt(1)
list.print()

list.deleteAt(1)
list.print()

list.deleteAt(0)
list.print()