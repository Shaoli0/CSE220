
    
def fibonacci(n):
    
    
    if n==1:
        return 0
    if n in [2,3]:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
    
print(fibonacci(5))

