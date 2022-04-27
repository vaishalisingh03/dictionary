dict=[{"V":"s001"},{"V":"s002"},{"VI":"s001"},{"VI":"s005"},{"VII":"s005"},
{"VI":"s009"},{"VII":"s007"}]
b=[]
for i in dict:
    for j in i.items():
        if j not in b:
            b.append(j)
print(b)