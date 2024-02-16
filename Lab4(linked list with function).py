# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 01:43:03 2021

@author: HP
"""


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
    def parenthesisBalancing(self,a):
        for i in a:
            if i=="(" or i=="{" or i=="[":
                stack1.push(i)

            elif i==")":
                if self.head is None:
                    print("Expression is Wrong!")
                    return 
                else:
                    store=stackl.pop()
                    if store!="(":
                        print("Expression is Wrong!")
                        return 
            elif i=="}":
                if self.head is None :
                    print("Expression is Wrong!")
                    return 
                else:
                    store=stackl.pop()
                    if store!="{":
                        print("Expression is Wrong!")
                        return     
            elif i=="]":
                if self.head is None:
                    print("Expression is Wrong!")
                    return 
                else:
                    store=stackl.pop()
                    if store!="[":
                        print("Expression is Wrong!")
                        return 
                
        if self.head is None:
            print("The expression is correct")
            
a="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
stack1=ListStack(a)
stack1.printList()
stack1.parenthesisBalancing(a)