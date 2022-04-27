d={"a":{"i":4,"o":9,},"b":{"v":6,"f":4}}
d1={}
for i ,j in d.items():
    if d[i]==j:
        d1.update({i:j})
    print(d1)



    