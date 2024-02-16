def fibonacci(n):
    if n==1:
        return 0
    elif n in [2,3]:
        return 1
    elif fibonacci_series[n] != -1: 
        return fibonacci_series[n]
    else:
        fibonacci_series_element=fibonacci(n-1)+fibonacci(n-2)
        fibonacci_series[n]=fibonacci_series_element
        return fibonacci_series[n]
n1=int(input("Enter the nth number: "))
fibonacci_series=[-1]*(n1+1)
print(fibonacci(n1))


