arr=[1,2,2,3,4,4,5]
unique=list(set(arr))
print(unique)


unique2=[]
for i in arr:
    if i not in unique2:
        unique2.append(i)
print(unique2)