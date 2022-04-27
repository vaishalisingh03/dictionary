dict=[{"id":1,"success":True,"name":"sai"},{"id":2,"success":False,"name":"shna"},
{"id":3,"success":True,"name":"sona"}]
user=input("enter name")
sum=0
for i in dict:
    sum+=i[user]
print(sum)

