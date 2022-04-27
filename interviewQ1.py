a={"a":{"course":10},"u":{"fees":10},"p":{"course":10,"p":10}}
sum=0
for i in a:
    if type(a[i])==dict:
        for j in a[i]:
            sum+=a[i][j]
    else:
        sum+=a[i]
print(sum)