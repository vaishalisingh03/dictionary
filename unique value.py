dict={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
d={}
for i in dict:
    dict.update({"ball":"red","bat":4})
    d.update(dict)
print(d)
