#Task-1
class KeyIndex:
    def __init__(self,a):
        c=0
        for b in range(len(a)):
            if a[b]<0:
                c+=1
                break
        if c!=0:
            minimum=a[0]
            for l in a:
                if l<minimum:
                    minimum=l
            self.x=minimum*(-1)
            for i in range(len(a)):
                temp=a[i]
                a[i]=temp+self.x
        else:
            self.x=0
        m=a[0]
        for y in range(len(a)):
            if a[y]>m:
                m=a[y]
        
        self.k=[0]*(m+1)
        
        for j in range(len(a)):
            index=a[j]
            self.k[index]=self.k[index]+1
            
    def search_method(self,element):
        value=element+self.x
        if value<0 or value>=len(self.k) or self.k[value]==0:
            return False
        else:
            return True
    def sort_method(self):
        for i in range(len(self.k)):
                if self.k[i]!=0:
                    increment=0
                    while increment<self.k[i]:
                        real_value=i-(self.x)
                        print(real_value,end=" ")
                        increment+=1
        print('')
#Tester
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
