dict1 =  {'Alex': ['subj1', 'subj3'], 'David': ['subj1', 'subj2',"opiu"]}
count=0
for i in dict1:
    j=0
    while j<len(dict1[i]):
        count+=1
        j+=1
print(count)