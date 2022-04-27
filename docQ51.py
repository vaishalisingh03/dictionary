dict={"v":[1,4,6,10],"vi":[1,4,12],"vii":[1,3]}
d={}
for i,y in dict.items():
      l=[]
      for j in y:
          if j%2==0:
              l.append(j)
              d.update({i:l})
print(d)


