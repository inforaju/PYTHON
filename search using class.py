class Search:
    def __init__(self):
        self.size=int(input("Enter the size: "))
        self.list=list()
        for i in range(0,self.size):
             item=int(input("Enter the item: "))
             self.list.append(item)
            
    def display(self):
        print("Size of the list: ",self.size)
        print("List: ",self.list)

    def linearsearch(self,target):
        i=0
        while (i<self.size):
          if self.list[i] == target:
              print("Target found at",i," position")
          i+=1      
        
              
    def binarysearch(self, target):
        left = 0
        right = len(self.list) - 1
        while (left <= right):
            mid = (left + right) // 2
            if self.list[mid] == target:
                print("Target found at ",mid,"position")
                break
            elif self.list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
           

        
ob=Search()
ob.display()
target=int(input("Enter your target: "))
b=ob.linearsearch(target)
c=ob.binarysearch(target)
