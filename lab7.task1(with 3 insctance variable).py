
class KeyIndex:
    def __init__(self,a):
        self.c=0
        for b in range(len(a)):
            if a[b]<0:
                self.c+=1
                break
        if self.c!=0:
            minimum=a[0]
            for l in a:
                if l<minimum:
                    minimum=l
            self.x=minimum*(-1)
            for i in range(len(a)):
                temp=a[i]
                a[i]=temp+self.x
        
        m=a[0]
        for y in range(len(a)):
            if a[y]>m:
                m=a[y]
        
        self.k=[0]*(m+1)
        
        for j in range(len(a)):
            index=a[j]
            self.k[index]=self.k[index]+1
    def search_method(self,element):
        if self.c!=0:
            value=element+self.x
            if value>=len(self.k) or value<0 or self.k[value]==0:
                return False
            else:
                return True
                
        else:
            if element<0 or self.k[element]==0 or element>=len(self.k):
                return False
            
            else:
                return True
    def sort_method(self):
        if self.c!=0:
            for i in range(len(self.k)):
                if self.k[i]!=0:
                    increment=0
                    while increment<self.k[i]:
                        real_value=i-(self.x)
                        print(real_value,end=" ")
                        increment+=1
        else:
            for i in range(len(self.k)):
                if self.k[i]!=0:
                    increment=0
                    while increment<self.k[i]:
                        print(i,end=" ")
                        increment+=1
        print('')

A=[4,2,3,4,7,4]
obj=KeyIndex(A)
print(obj.search_method(3))
obj.sort_method()

print("-------------")

A=[4,2,3,4,7,4]
obj=KeyIndex(A)
print(obj.search_method(0))
obj.sort_method()

print("-------------")
A=[4,2,3,4,7,4]
obj=KeyIndex(A)
print(obj.search_method(-9))
obj.sort_method()

print("-------------")

A=[4,2,3,4,7,4]
obj=KeyIndex(A)
print(obj.search_method(14))
obj.sort_method()

print("-------------")

A=[4,-2,3,-4,7,4]
obj=KeyIndex(A)
print(obj.search_method(-4))
obj.sort_method()                    

print("-------------")

A=[4,-2,3,-4,7,4]
obj=KeyIndex(A)
print(obj.search_method(0))
obj.sort_method()

print("-------------")

A=[4,-2,3,-4,7,4]
obj=KeyIndex(A)
print(obj.search_method(-1))
obj.sort_method()



