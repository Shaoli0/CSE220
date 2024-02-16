#Task-1
class Stack:
    def __init__(self , a):
        j=0
        for i in a:
            if i=="(" or i=="{" or i=="[":
                j+=1
        self.len=j
        self.l=[0]*self.len
        self.index=0
        self.pointer=-1
    def push(self,b):
        if self.pointer == (self.len-1):
            print("stack overflow!")
            return 
        else:
            self.l[self.index]= b
            self.index+=1
            self.pointer+=1
    def pop(self):
        if self.pointer==-1:
            print("Stack underflow!")
            return None
        else:
            val=self.l[self.pointer]
            self.index-=1
            self.pointer-=1
            return val  
    def printList(self):
        print(self.l)
    

class parenthesisBalancing:
    def __init__(self,a):
        stack1=Stack(a)
        

        for i in a:
            if i=="(" or i=="{" or i=="[":
              stack1.push(i)

            elif i==")":
                if stack1.pointer==-1:
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="(":
                        print("This Expression is not correct!")
                        return 
            elif i=="}":
                if stack1.pointer==-1:
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="{":
                        print("This expression is not correct!")
                        return     
            elif i=="]":
                if stack1.pointer==-1:
                    print("This expression is not correct!")
                    return 
                else:
                    store=stack1.pop()
                    if store!="[":
                        print("This expression is not correct!")
                        return 
                
        if stack1.pointer==-1:
            print("This expression is correct")
#Task-2
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
