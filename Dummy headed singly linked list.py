class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next
class DummyheadedList:
    def __init__(self):
        self.head=Node(None,None)
        self.head.next=None
    def insert(self,element):
        if self.head.next is None:
            self.head.next=Node(element,None)
        else:
            n=self.head.next
            while n.next!=None:
                n=n.next
            n.next=Node(element,None)
    def printList(self):
        if self.head.next==None:
            print("Empty List.")
        else:
            a=self.head.next
            while a is not None:
                print(a.value, end=" ")
                a=a.next
            print()
    
    
linkedlist=DummyheadedList()
linkedlist.insert(4)
linkedlist.printList()
linkedlist.insert(5)
linkedlist.printList()        
            
           
            

