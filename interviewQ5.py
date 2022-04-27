num=int(input("enter number"))
l=[]
l1=[]
for i in range(1,num):
    count=0
    for j in range(1,num):
        if i%j==0:
            count+=1
    if count==2:
        l.append(i)
    else:
        l1.append(i)
d={}
k=0
while k<len(l):
    d.update({l[k]:l1[k]})
    k+=1
print(d)

        