def insertion_sort(a):
    for i in range(1,len(a)):
        current=a[i]
        index=i
        while (current<a[index-1] and index>=1):
            a[index]=a[index-1]
            index-=1
        a[index]=current
            
A=[22,5,14,2,7,1]
insertion_sort(A)
print(A)

