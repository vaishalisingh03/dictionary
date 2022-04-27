dict={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,11]}
l=[]
for i,j in dict.items():
    print(i,end=" ")
    l.append(j)
print()
for x in range(len(l)):
    for y in range(len(l)):
        print(l[y][x],end="  ")
    print()