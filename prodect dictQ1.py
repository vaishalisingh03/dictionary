n=int(input("enter number"))
d={}
for i in range(1,n+1):
    c=i**i
    d.update({i:c})
print(d)

