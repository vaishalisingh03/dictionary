num=int(input("enter number"))
l=[]
for i in range(1,num):
    l.append(i)
print(l)
d={}
for i in range(len(l)):
    if l[i]%2==0:
        d.update({l[i]:"true"})
    else:
        d.update({l[i]:"false"})
print(d)