#Task-1
def powerN(base,n):
    if n==0:
        return 1
    if n==1:
        return base
    else:
        return base*powerN(base, n-1)
print(powerN(3,3))
#Task-3
def hocBuilder(height):
    if height==0:
        return 0
    elif height==1:
        return 8
    elif cards[height] != -1: 
        return cards[height]
    else:
        card_number=5+hocBuilder(height-1)
        cards[height]=card_number
        return cards[height]
    
n1=int(input("Enter the number of house of cards you want to build: "))
cards=[-1]*(n1+1)
b=hocBuilder(n1)        
if b!=0:
    print(f"you require {b} number of cards to build a house")
else:
    print("You do not build a house at all")
#Task-5
#(a)
def print_row(i,val):
     
    
    if (i == val):
        return
    print(i , end=" ")
 
    
    print_row(i+1,val)
 

def pattern(n):
    # base case
    if (n == 0):
        return
    
    pattern(n - 1)
    print_row(1,n+1)
    print("")

#(b)
def print_space(space):
    if (space == 0):
        return
    print(" ",end=" ")
    print_space(space - 1)
 

def value_print(i,val,n):
    if (val == n):
        return
    print(i, end=" ")
    value_print(i+1,val+1,n)
 
# function to print the pattern
def pattern(n):
    if (n == 0):
        return
    print_space(n-1)
    
    value_print(1,n-1,m)
    print()
    pattern(n-1)
    
    
m=5    
pattern(m)
#Task-6
class FinalQ:
        
    def Print(self,array,idx):
        if (idx<len(array)):
            profit=self.calcProfit(array[idx])
            print(f"Investment:{array[idx]};Profit:{profit}")
            self.Print(array,idx+1)
            
    def calcProfit(self,investment):
        def multi(x,y):
               
            if x==0:
                return 0
            else:
                return y + multi(y, x-1)
               
        if investment>=25000 and investment%100==0:
            if investment==25000:
                return 0
            elif investment<=100000:
                return multi(((investment-25000)/100),(4.5))
            else:
                return multi((75000/100),(4.5))+ multi(((investment-100000)/100),(8))
        else:
            print("Given investment is less than required")
  
        
        
        
#Tester
a=[25000,100000,250000,350000]
f=FinalQ()
f.Print(a,0)
#Task-7
def binary_search(a,b,A,B):
    lst = [0]*b
    for i in range(0,b):
        left=0
        right=a-1
        while left<=right:
            M=(left+right)//2
            if B[i]==A[M]:
                if left==right:
                    lst[i] = M+1
                    break
                elif B[i]==A[M+1]:
                    left=M+1
                else:
                    lst[i] = M+1
                    break
            elif B[i]>A[M]:
                if left==right:
                    lst[i]=M+1
                    break
                
                elif B[i]<A[M+1]:
                    lst[i] = M+1
                    break
                else:
                    left=M+1
            else: 
                if B[i]>A[M-1]:
                    lst[i] = M
                    break
                else:
                    right=M-1
    for i in lst:
        print(i,end=" ")

binary_search(5,1,[1,3,3,4,5],[2])
#Task-8
def game(n,string,player_avail,n_index,string_index):
    if n==1 and player_avail[n_index]!=-1:
        return n_index+1
    if player_avail[n_index]==-1:
        return game(n,string,player_avail,(n_index+1)%len(player_avail),string_index)
    else:    
        if string[string_index]=='2' or string[string_index]=='4':
            player_avail[n_index]=-1
            return game(n-1,string,player_avail,(n_index+1)%len(player_avail),(string_index+1)%len(player_avail))
        else:
            return game(n,string,player_avail,(n_index+1)%len(player_avail),(string_index+1)%len(player_avail))

N=3    
lst = '152'
list1=[0]*N
print(game(N, lst,list1,0,0)