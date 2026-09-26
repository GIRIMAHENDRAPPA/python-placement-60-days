def count_frequency(lst):
    freq={}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return freq
print(count_frequency([1,2,2,3,4,4,5]))