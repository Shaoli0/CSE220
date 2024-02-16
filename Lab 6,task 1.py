def minIndex(a,start,end):
    if start==end:
        return start
    index=minIndex(a, start+1, end)
    if a[index]<a[start]:
        return index
    else:
        
        return start

def selection(A,start,end):
    
    if start==end:
        return A
    min_index=minIndex(A,start,end)
    if (min_index!=start):
        temp=A[min_index]
        A[min_index]=A[start]
        A[start]=temp
    selection(A, start+1,end)
        

a=[1,5,4,3,2,9]
selection(a,0,len(a)-1)
print(a)

