def fac(m,n):
    if n==0:
        return 1
    if n==1:
        return m
    return m*fac(m,n-1)
print(fac(5,1))



