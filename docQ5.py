dict={1:2,3:4,4:3,2:1,0:0}
l=[]
for i in dict:
    l.append(dict[i])
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]>l[j]:
            c=l[i]
            l[i]=l[j]
            l[j]=c
        j+=1
    i+=1
dict1={}
p=[]
for k in range(len(l)):
    for i,j in dict.items():
        if j==l[k]:
            dict1.update({i:l[k]})
            # p.append((i,l[k]))
print(dict1)
# print(p)

