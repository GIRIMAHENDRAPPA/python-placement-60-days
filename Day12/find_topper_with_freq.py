marks={"Aman":85,"rahul":90,"simran":85,"priya":90,"raj":70}

from collections import Counter
freq=Counter(marks.values())
print(freq)

max_mark=max(marks.values())
toppers=[name for name,m in marks.items() if m ==max_mark]
print(toppers)