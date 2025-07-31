class Pair_elements:
    def sum(self,num,target):
        Lookup={}
        for i,n in enumerate(num):
            if target-n in Lookup:
                return(Lookup[target-n],i)
            Lookup[n]=i
value=int(input("enter the sum"))
print(Pair_elements().sum((10,20,30,40,50,60,70),value))