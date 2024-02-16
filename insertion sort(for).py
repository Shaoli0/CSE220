def insertion_sort(A):

  for i in range(1,len(A)):

    for j in range(i-1,-1,-1):

      if(A[j]>A[j+1]):

        temp = A[j]

        A[j]=A[j+1]

        A[j+1]=temp

      else:

        break


A=[22,5,14,2,7,1]
insertion_sort(A)
print(A)