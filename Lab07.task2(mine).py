def hashTable(a):
    hash_table=[-1]*(len(a))
    vowels="AEIOU"
    numbers="123456789"
    s=0
    c=0
    for i in range(len(a)):
        temp=a[i]
        for j in range(len(temp)):
            if temp[j] in numbers:
                s=s+int(temp[j])
            if temp[j] not in vowels:
                c+=1
        index=((c*24)+s)%9
        if hash_table[index]==-1:
            hash_table[index]=temp
        else:
            count=0
            if index>(len(hash_table)-1):
                index=0
            while hash_table[index]!=-1 or count!=len(hash_table):
                if index==len(hash_table):
                    index=0
                else:
                    index=index+1
                count+=1
            if hash_table[index]==-1:
                hash_table[index]=temp
            if count==len(hash_table):
                print("the string",temp,"can not be placed in the hashtable as there is no empty index left")
    for k in range(len(hash_table)):
        print(hash_table[k],end=" ")

A=["ST1E89B8A32","AB3J88IB45","IK4L32FA71"]
hashTable(A)
               
                


