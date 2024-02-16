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
    def showList(self):
        if self.head==None:
            print("Empty List.")
        else:
            
            p=self.head
            while p is not None:
                print(p.value, end="    ")
                p=p.next
            print()
    def bubble_sort(self):
        end=None
        while end!=self.head.next:
            current=self.head
            while current.next!= end:
                next_node=current.next
                if current.value>next_node.value:
                    current.value,next_node.value=next_node.value,current.value
                current=current.next
            end=current
b=[9,3,5,2]
myList=singleLinkedList(b)
myList.showList()
myList.bubble_sort()
myList.showList()
