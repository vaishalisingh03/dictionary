dict={"1":["a","b"],"2":["c","d"]}
d=list(dict.values())
for i in d[0]:
    for j in d[1]:
        print(i+j)