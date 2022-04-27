id=[1,2,3,4]
n=["a","b","c","d"]
a=[12,6,8,9]
d={}
for i in  range(len(id)):
    d1={}
    for j in range(len(n)):
        if i==j:

            d1.update({n[j]:a[j]})
    d.update({id[i]:d1})
print(d)


