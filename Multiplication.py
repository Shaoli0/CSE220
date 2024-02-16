def product( x , y ):
    
    if x==1:
        return y
    if y==1:
        return x
    if x==0 or y==0:
        return 0
    else:
        return y+product(y, x-1)
 

x = 100000/100
y = 4.5
print( product(x,y))

