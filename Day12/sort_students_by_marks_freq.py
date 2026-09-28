marks=[85,90,85,70,90,90]

from collections import Counter
freq=Counter(marks)

sorted_by_freq=sorted(marks,key=lambda x:freq[x],reverse=True)

final=[]
seen=set()
for m in sorted_by_freq:
    if m in sorted_by_freq:
        seen.add(m)
        final.append(m)
print(final)
