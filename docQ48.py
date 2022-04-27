dict={1:"red",2:"green",3:"black",4:"white",5:"black"}
d={}
for i in dict:
    k=len(dict[i])
    d.update({dict[i]:k})
print(d)