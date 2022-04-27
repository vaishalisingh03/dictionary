dict = {'a':50, 'b':58, 'y':89,'c':56,'d':40, 'e':100, 'f':20,"y":90,"o":78}
max1=0
max2=0
max3=0
d=[]
for i in dict:
    for j in dict:
        if dict[j]>max1:
            max1=dict[j]
        if dict[j]>max2 and dict[j]!=max1:
                 max2=dict[j]
        if dict[j]>max3 and dict[j]!=max1 and dict[j]!=max2:
                max3=dict[j]
d.append(max1)
d.append(max2)
d.append(max3)
print(d)