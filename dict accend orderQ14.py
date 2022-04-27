dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
l=[]
for x in dict:
    l.append(dict[x])
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            c=l[i]
            l[i]=l[j]
            l[j]=c
        j+=1
    i+=1
dict1={}
for k in range(len(l)):
    for i,j in dict.items():
        if j==l[k]:
            dict1.update({i:l[k]})
print(dict1)




