marks=[85,90,85,70,90,90]

seen=set()
unique_ordered=[]
for m in marks:
    if m is not seen:
        seen.add(m)
        unique_ordered.append(m)
print(unique_ordered)