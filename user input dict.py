num=int(input("enter number"))
dict={}
for i in range(num):
    key=input("enter keys")
    value=input("enter value")
    dict.update({key:value})
print(dict)