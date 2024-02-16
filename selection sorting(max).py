def minIndex(a,m,i):
    if m==i:
        return m
    index=minIndex(a, m+1, i)
    if a[index]<a[m]:
        return index
    else:
        return m

    
    
    
def selection(A,start,end):
    
    if size==0:
        return A
    min_index=minIndex(A,start+1,end)
    if (min_index!=start):
        temp=A[min_index]
        A[min_index]=A[start]
        A[start]=temp
    selection(A, start+1,end)
        
    
        
        for j in range(0,i):
            if (A[j]>m):
                m=A[j]
                max_index=j
        

a=[1,5,4,3,2,9]

selection(a,0,len(a)-1)
print(a)        

