class Node:
    def __init__(self, value):
        self.prev = None
        self.info = value
        self.link = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def insert_at_beginning(self, value):
        t = Node(value)
        if self.start == None:
            self.start = t
        else:
            p = self.start
            self.start = t
            t.link = p
            p.prev = t

    def insert_at_end(self, value):
        t = Node(value)
        if self.start == None:
            self.start = t
        else:
            p = self.start
            while p.link != None:
                p = p.link
            p.link = t
            t.prev = p

    def delete_at_beginning(self):
        if self.start == None:
            print("Empty linked list")
            return
        else:
            p = self.start
            self.start = p.link
            if self.start != None:
                self.start.prev = None
            item = p.info
            del p
            return item

    def delete_at_end(self):
        if self.start == None:
            print("Empty linked list")
            return
        else:
            p = self.start
            while p.link != None:
                p = p.link
            if p.prev != None:
                p.prev.link = None
            else:
                self.start = None
            item = p.info
            del p
            return item

    def insert_at_specific_pos(self, pos, value):
        t = Node(value)
        if pos == 1:
            t.link = self.start
            if self.start != None:
                self.start.prev = t
            self.start = t
        else:
            p = self.start
            i = 1
            while i != pos-1 and p != None:
                p = p.link
                i += 1
            if p == None:
                print("Position not found")
            else:
                t.link = p.link
                t.prev = p
                if p.link != None:
                    p.link.prev = t
                p.link = t

    def delete_at_specific_pos(self, pos):
        if pos == 1:
            p = self.start
            self.start = p.link
            if self.start != None:
                self.start.prev = None
            item = p.info
            del p
            return item
        else:
            p = self.start
            i = 1
            while i != pos-1 and p != None:
                p = p.link
                i += 1
            if p == None or p.link == None:
                print("Position not found")
            else:
                item = p.link.info
                q = p.link
                r = q.link
                p.link = r
                if r != None:
                    r.prev = p
                del q
                return item
            
    def delete_after_item(self, x):
        if self.start is None:
            print("Empty linked list")
            return

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None or p.link is None:
            print(f"No node found after {x}")
            return

        q = p.link
        p.link = q.link
        if q.link is not None:
            q.link.prev = p
        del q
        
    def insert_after_item(self, x, value):
        if self.start is None:
            print("Empty linked list")
            return

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(f"{x} not found in the linked list")
            return

        t = Node(value)
        t.link = p.link
        t.prev = p
        if p.link is not None:
            p.link.prev = t
        p.link = t
        

    def display(self):
        if self.start == None:
            print("Empty linked list")
        else:
            p = self.start
            while p.link != None:
                print(p.info, end=" ")
                p = p.link
            print(p.info)

d1 = DoublyLinkedList()
d1.insert_at_beginning(20)
d1.insert_at_beginning(10)
d1.insert_at_specific_pos(3,30)
d1.display()
d1.delete_at_specific_pos(2)
d1.display()
d1.insert_after_item(30, 40)
d1.display()
d1.delete_after_item(40)
d1.display()
