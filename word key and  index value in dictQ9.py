word="mississippi"
dict={}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)