dict1={1:2}
dict2={3:4}
dict3={4:7}
i=0
l={}
while i<len(dict1):
    l.update(dict1)
    l.update(dict2)
    l.update(dict3)
    i+=1
print(l)

