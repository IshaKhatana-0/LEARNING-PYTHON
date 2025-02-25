tup=(1,4,9,16,25,36,49,64,81,100)
i=int(input("enter number you want to search"))
n=0
while n<len(tup):
    if(tup[n]==i):
      print(i , "is present at", n, "index in tuple")
    n=n+1
  