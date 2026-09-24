arr=[10,20,5,40,15,40]
print("largest:",max(arr))
largest=second=-1
for num in arr:
    if num > largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print("second largest:",second)