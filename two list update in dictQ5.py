list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
d={}
i=0
while i <len(list1):
    d.update({list1[i]:list2[i]})
    i+=1
print(d)
