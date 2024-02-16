
class Node:
    def __init__(self,element):
        self.element=element
        self.next=None
        
class ListStack:
    def __init__(self):
        self.head=None
        
    def push(self,element):
        n=Node(element)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
            
        
    def pop(self):
        if self.head is None:
            print("Stack underflow")
            return None
        else:
            n1=self.head
            self.head=self.head.next
            n1.next=None
            return n1.element
        
    def peek(self):
        if self.head is None:
            print("Stack underflow")
            return None
        else:
            return self.head.element
    def printList(self):
        if self.head==None:
            print("Empty List.")
        else:
            
            a=self.head
            while a is not None:
                print(a.element, end="    ")
                a=a.next
            print()
class parenthesisBalancing:
    def __init__(self,a):
        stack1=ListStack()
        
        for i in a:
            if i=="(" or i=="{" or i=="[":
                stack1.push(i)

            elif i==")":
                if stack1.head is None:
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="(":
                        print("This expression is not correct!")
                        return 
            elif i=="}":
                if stack1.head is None :
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="{":
                        print("This expression is not correct!")
                        return     
            elif i=="]":
                if stack1.head is None:
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="[":
                        print("This expression is not correct!")
                        return 
                
        if stack1.head is None:
            print("This expression is correct")     
        
a="1+2*(3/4)"
parenthesisBalancing(a)
 
a="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
parenthesisBalancing(a)

a="1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
parenthesisBalancing(a) 

a="1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"  
parenthesisBalancing(a)      