
class stack:
    def __init__(self,size):
        self.list=[]
        self.size=size
        self.top=-1
    def push(self,item):
        if self.top==self.size-1:
            print("stack is full")
            
        else:
            self.top+=1
            self.list.append(item)
            print(self.list)
    def display(self):
        print(self.list)
    def pop(self):
        if self.top==-1:
            print("stack is empty")
            return -1
        else:
            item1=self.list[self.top]
            self.list.pop(self.top)
            self.top-=1
            return item1
    def peek(self):
        if self.list!=[]:
            return self.list[self.top]
        else :
            return -1
        

ob=stack(10)  
print(ob.peek())

post=[]
string=input("Enter the infix expression: ")
list=string.split()
print(list)
oper=['+','-','*','/']
def precedence(a):

    if i=="*" or i=="/":
        print(i,end=" ")
        return 2

    elif i=="+" or i=="-":
        print(i,end=" ")
        return 1
for i in list:
    if i=="(" :
        print(" left parenthesis")
        ob.push(i)
    elif i==")":
        print("right parenthesis")
        while ob.peek()!="(":
            post.append(ob.pop())
        ob.pop()
    
    elif i in oper: 
        while(True):
            if ob.peek()==-1:
                ob.push(i)
                break
            elif ob.peek()=="(":
                ob.push(i)
                break
            else:
                if precedence(i)<=precedence(ob.peek()):
                    post.append(ob.pop())
                else:
                    ob.push(i)
                    break
    else:
        post.append(i)
    print('Symbol',i)
    ob.display()
    print('Postfix',post)
while(ob.peek()!=-1):
    post.append(ob.pop())
print(post)
