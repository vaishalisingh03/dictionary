num=int(input("enter number of items"))
dict={}
for i in range(num):
    keys=input("enter keys")
    value=input("enter value")
    dict.update({keys:value})
print(dict)
name=input("enter keys")
if name in dict:
    print("yes this kyes in dict")
else:
    print("no this kyes is not in dict")

