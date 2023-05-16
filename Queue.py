class queue:
    def __init__(self,s):
        self.rear=-1
        self.front=-1
        self.size=s
        self.qu=[0 for i in range(s)]
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("queue is full")
            return
        self.rear=self.rear+1
        self.qu[self.rear]=item
        if self.front == -1:
            self.front =0
            
        
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
            return
        else:
            item=self.qu[self.front]
            #self.qu.pop(self.front)
            if self.front==self.rear:
                self.rear=-1
                self.front=-1
            
            else:
                self.front=self.front+1
            return item
    def display(self):
        if self.front==-1 and self.rear==-1:
            print('queue is empty')
            return
        for i in range(self.front,self.rear+1):
            print(self.qu[i],'<-',end=' ')
        print()
        
        
            
ob=queue(5)
ob.enqueue(20)
ob.enqueue(30)
ob.enqueue(23)
ob.enqueue(45)
ob.display()
ob.dequeue()
ob.dequeue()
ob.dequeue()
# ob.dequeue()
# ob.dequeue()
ob.display()


