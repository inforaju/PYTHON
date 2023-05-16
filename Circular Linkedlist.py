class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_first(data)
        else:
            new_node = Node(data)
            curr = self.head
            count = 1
            while count < pos and curr.next != self.head:
                curr = curr.next
                count += 1
            new_node.next = curr.next
            curr.next = new_node

    def delete_at_first(self):
        if not self.head:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next

    def delete_at_last(self):
        if not self.head:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            prev.next = self.head

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
        elif pos == 0:
            self.delete_at_first()
        else:
            curr = self.head
            prev = None
            count = 0
            while count < pos and curr.next != self.head:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next

    def display(self):
        if not self.head:
            print("List is empty")
        else:
            curr = self.head
            while True:
                print(curr.data, end=" ")
                curr = curr.next
                if curr == self.head:
                    break
            print()


clist = CircularLinkedList()

clist.insert_at_last(1)
clist.insert_at_last(2)
clist.insert_at_last(3)
clist.insert_at_last(4)
clist.insert_at_first(0)
clist.insert_at_position(5, 2)

clist.display() 

clist.delete_at_first()
clist.delete_at_last()
clist.delete_at_position(2)

clist.display()  
