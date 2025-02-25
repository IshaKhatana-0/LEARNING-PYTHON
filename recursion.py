'''def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n

s=sum(5)
print(s)'''


def list(l,index=0):
    if (index == len(l)):
        return
    print(l[index])
    list(l,index+1)

a=["a","b","c"]
list(a)