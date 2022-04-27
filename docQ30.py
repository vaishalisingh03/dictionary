dict={"s  001":["math","science"],"s  002":["math","sceince"]}
l={}
for i in dict:
    for x in i:
        k=i.replace(" ","")
        for j,p in dict.items():
            l.update({k:p})
print(l)