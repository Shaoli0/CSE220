class FinalQ:
        
    def Print(self,array,idx):
        if (idx<len(array)):
            profit=self.calcProfit(array[idx])
            print(f"investment:{array[idx]};Profit:{profit}")
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


