class Node:
    def __init__(self,value,next,prev):
        self.value=value
        self.next=next
        self.prev=prev
class DoublyLinkedList:
    def __init__(self,a):
        self.head=None
        tail=self.head
        for i in a:
            n=Node(i,None,None)
            if self.head is None:
                n.prev=self.head
                self.head=n
                tail=n
            else:
                tail.next=n
                n.prev=tail
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
    def insertion_sort(self):
        next_node=self.head.next
        while next_node is not None:
            firstnode=self.head
            while firstnode is not None:
                if (firstnode.value>next_node.value):
                    temp=firstnode.value
                    firstnode.value=next_node.value
                    next_node.value=temp
                
                
                else:
                    break
                firstnode=firstnode.next
            next_node=next_node.next 
    

b=[9,3,5,2]
myList=DoublyLinkedList(b)
myList.printList()
myList.insertion_sort()
myList.printList()
