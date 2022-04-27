dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
max1=0
max2=0
max3=0
p=[]
for i in dict:
    for j in dict:
        if dict[j]>max1:
            max1=dict[j]
            k=j
        if dict[j]>max2 and dict[j]!=max1:
            max2=dict[j]
            l=j
        if dict[j]>max3 and dict[j]!=max1 and dict[j]!=max2:
            max3=dict[j]
            m=j
p.append(k)
p.append(l)
p.append(m)
print(p)



