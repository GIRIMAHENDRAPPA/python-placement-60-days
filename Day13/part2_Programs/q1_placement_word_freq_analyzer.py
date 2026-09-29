para="LPU placement placement drive python python python java"

words=para.lower().split()
unique_words=set(words)

print(f"Total words:{len(words)}")
print(f"Unique words:{len(unique_words)}")

from collections import Counter
freq=Counter(words)
print("most common word:",freq.most_common(1))

unique_para=" ".join(set(words))
print(unique_para)