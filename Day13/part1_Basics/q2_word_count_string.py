text="python is easy and python is powerful"
words=text.split()

from collections import Counter
count=Counter(words)
print(count)

freq={}
for w in words:
    freq[w]=freq.get(w,0)+1
print(freq)