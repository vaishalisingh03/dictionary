dict={"a":1,"b":30,"c":20,"d":11}
l=[]
for i in dict:
    l.append(dict[i])
i=0
max=0
mini=l[0]
while i<len(l):
    if l[i]>max:
        max=l[i]
    if l[i]<mini:
        mini=l[i]
    i+=1
print(max)
print(mini)