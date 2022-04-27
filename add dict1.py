d1={1:10,2:20}
d2={3:30,2:40}
d3={5:50,6:60}
for i in (d2):
    if i in d1:
      d1[i]=d1[i]+d2[i]
      d1.update(d3)
    else:
        d1[i]=d2[i]
print(d1)


