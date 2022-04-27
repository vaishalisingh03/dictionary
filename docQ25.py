num=int(input("number items"))
dict={}
for i in range(num):
    world=input("enter string")
    for i in world:
        if i  in dict:
            dict[i]+=1
        else:
            dict[i]=1
print(dict)

        
