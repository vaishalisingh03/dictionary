dict=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"}, {"five":"5"}, 
{"six":"9"},{"seven":"7"}]
k=[]
for i in dict:
    for j in i:
        if i[j] not in k:
            k.append((i[j]))
print(k)