


class Node:
    def __init__(self,value,next,prev):
        self.value=value
        self.next=next
        self.prev=prev
class DoublyList:
    def __init__(self,a):
        self.head=Node(None,None,None)
        
        a=self.head
        
        self.head.next=self.head.prev
        self.head.prev=self.head
        
        for i in a:
            n =Node(i, None, None)
            n.next = a.next
            n.prev = a
            a.next = n
            a = n
        
    def showList(self):
        if self.head is None:
            print("Empty List.")
        else:
           i = self.head.next
           while i is not self.head:
               print(i.value)
           i = i.next
           
    def insert(self,newElement):
        b = self.head.next
        while b is not self.head:
            if b.value==newElement:
                print("Can't include the element as it already exists")
                return
            b =b.next
        temp=Node(newElement,None,None)
        b=self.head
        while b.next is not None:
            b=b.next
        b.next=temp
        temp.prev=b
    def inserAtIndexWithElement(self,newElement,index):
        count=0  
        a = self.head.next
        while a is not self.head:
            a=a.next
            count=count+1
        if index < 0 or index > count-1:
            print("Invalid Index!")
            return
        b=self.head
        while b is not None:
            if b.value==newElement:
                print("Can't include the element as it already exists")
                return
            b=b.next
        
        if index==0:
            a=Node(newElement,None,None)
            a.next=self.head
            self.head.prev=a
            self.head=a
            return
        else:
            b = self.head.next
            ind = 0
            while b is not self.head:
                
                if ind == index:
                    b = b.prev
                    n = Node(newElement,b.next,b)
                    b.next = n
                    n.next.prev = n
                    return
                ind=ind+1
                b = b.next
            
    def insertIndex(self,index):
        count=0  
        a = self.head.next
        while a is not self.head:
            a=a.next
            count=count+1
        if index < 0 or index > count:
            print("Invalid Index!")
            return
        
        else:
            count = 0
            a = self.head.next
            while a is not self.head:
                if count == index:
                    a.prev.next = a.next
                    a.next.prev = a.prev
                    a.value=None
                    a.next=None
                    a.prev=None
                    return
                a = a.next
                count=count+1
            
        
        
        
    def remove(self,deletekey):
        count = 0
        a = self.head.next
        while a is not self.head:
            if count == deletekey:
                 a.prev.next = a.next
                 a.next.prev = a.prev
                 a.value=None
                 a.next=None
                 a.prev=None
                 return deletekey
            a = a.next
            count=count+1

x=DoublyList([10,20,30,40,50])       
x.showList()        
x.insert(4)
x.showList()
x.inserAtIndexWithElement(5,0)
x.showList()
x.insetIndex(10)
x.showlist()
x.remove(3)
x.showList()       
        
    
        
                    