def binary_search(a,b,A,B,left,right):
    if left<=right:
        M=(left+right)//2
        if B[]==A[M]:
            return M+1
        elif B[]>A[M]:
            if B[]<A[M+1]:
                return M+1
            else:
                return binary_search(a,b,A,B,M+1,right)
        elif (B[]<A[M]):
            if B[]>A[M-1]:
                return M
            else:
                return binary_search((a,b,A,B,left,M-1)
    

    
    
    
    
    
    
C=[1,3,5,7,9]
D=[6,4,8]
binary_search(len(C),len(D),C,D,0,len(c)-1)