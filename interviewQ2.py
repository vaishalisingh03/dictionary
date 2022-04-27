dic=[{"name":"sakshi","age":17},{"name":"anju","age":18},{"name":"vaishu","age":9}]
a=[]
for i in range(len(dic)):
    for x,y in dic[i].items():
        if x=="age":
            a.append(y)
print(a)
