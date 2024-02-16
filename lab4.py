


class Stack:
    def __init__(self , a):
        j=0
        for i in a:
            if i=="(" or i=="{" or i=="[":
                j+=1
        self.len=j
        self.l=[]#creating an opening brackets list
        self.index=0
        self.index1=0
    def push(self,b):
        if self.index == self.len:
            print("stack overflow!")
            return
        else:
            self.l.insert(self.index, b)
            self.index+=1
    def pop(self):
        if self.pointer==-1:
            print("Stack underflow!")
            return None
        else:
            val=self.l[self.pointer]
            self.l=self.l[:-1]
            self.pointer-=1
            return val  #delete the last value existing in a list
    def peek(self):
        if self.pointer==-1:
            print("Stack Underflow!")
            return None
        return self.l[self.pointer]
    def printStack(self):
        print(self.l)

    def parenthasisBalancing(self,a):
        
        for j in a:
            self.index1+=1
            for i in a:
                if i=="(" or i=="{" or i=="[":
                    self.l.push(i)

                elif i==")":
                    if len(self.l)==0:
                        print("Expression is Wrong!")
                        print("Error at charecter #",self.index1,"not opened")
                        return False
                
                    else:
                        store=self.l.pop()
                        if store!="(":
                            print("Expression is Wrong!")
                            print("Error at charecter #",self.index1,"not closed")
                            return False
                 elif i=="}":
                     
                     if len(self.l)==0:
                         print("Expression is Wrong!")
                         print("Error at charecter #",self.index1,"not opened")
                         return False
                     else:
                         store=self.l.pop()
                         if store!="{":
                             print("Expression is Wrong!")
                              print("Error at charecter #",self.index1,"not closed")
                             return False   
                 elif i=="]":
                     if len(self.l)==0:
                         print("Expression is Wrong!")
                         print("Error at charecter #",self.index1,"not opened")
                         return False
                     else:
                         store=self.l.pop()
                         if store!="[":
                             print("Expression is Wrong!")
                             print("Error at charecter #",self.index1,"not closed")
                             return False
        if self.l==[]:
            print("The expression is correct")
a="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
stack1=Stack(a)
stack1.printStack()
stack1.parenthasisBalancing(a)