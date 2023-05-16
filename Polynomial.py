class Node:
    def __init__(self,c,e):
        self.c = c
        self.e = e
        self.link = None
        
class Polynomial:
    def __init__(self):
        self.start = None
        
    def add_node(self,c,e):
        if self.start == None:
            t = Node (c,e)
            self.start = t
            return
        else:
            prev = None
            p = self.start
            while (p != None and p.e != e):
                p = p.link
            if p != None:
                p.c += c
                return
            if p == None:
                t1 = self.start
                prev = None
                while t1 != None and t1.e > e:
                    prev = t1
                    t1 = t1.link
                if t1 == None:
                    tnew = Node(c,e)
                    prev.link = tnew
                else:
                    tnew = Node(c,e)
                    if prev == None:
                        tnew.link = t1
                        self.start = tnew
                    else:
                        tnew.link = t1
                        prev.link = tnew
                        
    def addition(self,P2):
        P3 = Polynomial()
        n = self.start
        t = P2.start
        while (n != None and t != None):
            if n.e > t.e:
                q = Node(n.c,n.e)
                n = n.link
            elif t.e > n.e:
                q = Node(t.c,t.e)
                t = t.link
            else:
                q = Node(t.c+n.c,n.e)
                n = n.link
                t = t.link
                
            if P3.start == None:
                P3.start = q
                prev = q
            else:
                prev.link = q
                prev = q
                
        while(t != None):
            q = Node(t.c , t.e)
            t = t.link
            prev.link = q
            prev = q
            
        while(n != None):
            q = Node(n.c , n.e)
            n = n.link
            prev.link = q
            prev = q
            
        return P3
    
    def multiplication(self,P2):
        P3 = Polynomial()
        n = self.start
        while n != None:
            t = P2.start
            while t != None:
                c = n.c * t.c
                e = n.e + t.e
                P3.add_node(c,e)
                t = t.link
            n = n.link
        return P3
            
    def display(self):
        p = self.start
        while p != None:
            print(p.c, "x^", p.e, end=" ")
            p = p.link
        print()
        
        
# Create the first polynomial
P1 = Polynomial()
P1.add_node(3, 5)
P1.add_node(2, 3)
P1.add_node(4, 0)

# Create the second polynomial
P2 = Polynomial()
P2.add_node(1, 4)
P2.add_node(2, 3)
P2.add_node(3, 2)
P2.add_node(1, 0)

# Display the first polynomial
print("P1: ", end="")
P1.display()
print()

# Display the second polynomial
print("P2: ", end="")
P2.display()
print()

# Add the two polynomials
P3 = P1.addition(P2)
P4 = P1.multiplication(P2)

# Display the result
print("P3: ", end="")
P3.display()
print()

print("P4: ", end="")
P4.display()
print()
