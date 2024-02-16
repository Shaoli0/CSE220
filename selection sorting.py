def selection_sorting(a):
    for i in range(len(a)-1):
        min_index=i
        for j in range(i,len(a)):
            if (a[j]<a[min_index]):
                min_index=j
        temp=a[i]
        a[i]=a[min_index]
        a[min_index]=temp
        
            
A=[22,5,14,2,7,1]
selection_sorting(A)
print(A)   


