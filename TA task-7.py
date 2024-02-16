def binary_search(a,b,A,B):
    left=0
    right=a-1
    while left<=right:
        M=(left+right)//2
        if B[i]==A[M]:
            if left==right:
                return M+1
                break
            elif B[i]==A[M+1]:
                left=M+1
            else:
                return M+1
                break
        elif B[i]>A[M]:
            if left==right:
                return M+1
                break
                
            elif B[i]<A[M+1]:
                return M+1
                break
            else:
                left=M+1
        else:
            if B[i]>A[M-1]:
                return M
                break
            else:
                right=M-1
    return 0
C=[2,5,5,5,5,6]
D=[5,1,7]
array=[0]*len(D)
for i in range(len(D)):
    array[i]=binary_search(len(C),len(D), C, D)
    
print(array)

