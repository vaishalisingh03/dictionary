# dict={"a":{"drt":1,"o":90},"b":{"vy":8,"yu":"e"}}
# p={"drt":56,"o":10}
# dict["a"]=p
# print(dict)


l=["a","b","c","d"]
i=0
while i<len(l):
    j=0
    d={}
    while j<len(l):
        d.update({l[j]:j})
        j+=1
    i+=1
print(d)