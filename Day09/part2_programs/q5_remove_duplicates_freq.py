arr = [1,1,2,3,2,1,4]

# Remove duplicates
unique = list(set(arr))
print("Unique:", unique)

# Frequency - DICT - 100% asked
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print("Frequency:", freq)