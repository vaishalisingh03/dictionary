num=int(input("enter number of elements"))
dict={}
for i in range(num):
    key=input("enter keys")
    value=input("enter values")
    dict.update({key:value})
print(dict)