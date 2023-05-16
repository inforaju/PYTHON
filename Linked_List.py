class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_first(data)
        else:
            new_node = Node(data)
            current = self.head
            prev = None
            count = 0
            while current and count < pos:
                prev = current
                current = current.next
                count += 1
            if current is None and count == pos:
                prev.next = new_node
            elif current:
                new_node.next = current
                prev.next = new_node
            else:
                print("Invalid position")

    def delete_at_first(self):
        if self.head:
            self.head = self.head.next

    def delete_at_last(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None

    def delete_at_position(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.delete_at_first()
        else:
            current = self.head
            prev = None
            count = 0
            while current and count < pos:
                prev = current
                current = current.next
                count += 1
            if current is None and count == pos:
                prev.next = None
            elif current:
                prev.next = current.next
            else:
                print("Invalid position")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinkedList()

linked_list.insert_at_first(3)
linked_list.insert_at_first(2)
linked_list.insert_at_first(1)
linked_list.insert_at_last(4)
linked_list.insert_at_position(5, 2)

linked_list.display()  

linked_list.delete_at_first()
linked_list.delete_at_last()
linked_list.delete_at_position(1)

linked_list.display()  
