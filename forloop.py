"""tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number to be searched"))
i=0
for val in tuple:
    if(x==tuple[i]):
        print(x , "is found in tuple at index ",i)
        break
    i=i+1
else:
    print(x, "is not present in the tuple")   """


n=int(input("enter the value of n"))
i=0,sum=0
while i<=n:
    print(sum+i)
    i=i+1
print("the sum of first ",n ,"numbers is", sum)
    
    
    
    