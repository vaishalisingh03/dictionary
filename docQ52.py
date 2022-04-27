dict={"a":5,"b":14,"c":32,"d":35,"e":246,"f":100,"g":57,"h":8,"i":10}
max1=0
max2=0
max3=0
max4=0
max5=0
l=[]
for i in dict:
    for j in dict:
        if dict[j]>max1:
            max1=dict[j]
            m=j
        if dict[j]>max2 and dict[j]!=max1:
            max2=dict[j]
            k=j
        if dict[j]>max3 and dict[j]!=max1 and dict[j]!=max2:
            max3=dict[j]
            y=j
        if dict[j]>max4 and dict[j]!=max1 and dict[j]!=max2 and dict[j]!=max3:
           max4=dict[j]
           c=j
l.append(m)
l.append(k)
l.append(y)
l.append(c)
print(l)