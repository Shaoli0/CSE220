def binary_search(A, value,left,right):
    if left<=right:
        M=(left+right)//2
        if(value==A[M]):
            return M
        elif (value>A[M]):
            return binary_search(A, value, M+1, right)
        elif (value<A[M]):
            return binary_search(A,value,left,M-1)
    else:
        return -1
a=[5,6,12,19,20,30]
answer=(binary_search(a, 0, 0, len(a)-1))
if (answer==-1):
    print("The given value does not exist in the list")
    
else:
    print("the index number of the element is :", answer)
    
  