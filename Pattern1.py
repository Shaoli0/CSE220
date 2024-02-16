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
    
    pattern(n - 1)
    print_row(n)
    print("")

pattern(5)


