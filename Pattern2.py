def print_row(val):
     
    # base case
    if (val == 0):
        return
    print(val , end=" ")
 
    # recursively calling print_row()
    print_row(val-1)
 
# function to print the pattern
def pattern(n):
    # base case
    if (n == 0):
        return
    print_row(n-n+1)
    print("")
 
    # recursively calling pattern()
    pattern(n - 1)

pattern(5)


