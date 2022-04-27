dict={1:["vaishu singh"],2:["anju singh"],3:["nishu singh"],4:["nidhi singh"],
5:["siya singh"]}
l=[]
for i in dict:
    l.append(dict[i])
b=[]
for i in range(len(l)):
        for j in range(len(l[i])):
            b.append(l[i][j])
d={}
count=0
for x in range(len(b)):
    count+=1
    for j in range(len(b[x])):
            d.update({count:b[x]})
print([d])



