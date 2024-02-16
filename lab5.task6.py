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
                    

def addition(head):
    if head is None:
        return 0
    else:
        return (head.value)+addition(head.next)
b=[9,3,5,2]
myList=singleLinkedList(b)

print(addition(myList.head))     
