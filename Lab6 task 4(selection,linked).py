class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next
class singleLinkedList:
    def __init__(self,a):
        self.head=None
        tail=self.head
        for i in a:
            n=Node(i, None)
            if self.head is None:
                self.head=n
                tail=self.head
            else:
                tail.next=n
                tail=n
    def printList(self):
        if self.head==None:
            print("Empty List.")
        else:
            p=self.head
            while p is not None:
                print(p.value, end=" ")
                p=p.next
            print()
    def selection_sort(self):
        firstnode=self.head
        while firstnode is not None:
            
            minimum=firstnode
            next_node=firstnode.next
            
            while next_node is not None:
                if (minimum.value>next_node.value):
                    minimum=next_node
                next_node=next_node.next
                
            temp=firstnode.value
            firstnode.value=minimum.value
            minimum.value=temp
            firstnode=firstnode.next
b=[9,3,5,2]
myList=singleLinkedList(b)
myList.printList()            
myList.selection_sort()
myList.printList()        

