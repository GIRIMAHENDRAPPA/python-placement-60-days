def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2]
print(second_largest([1, 2, 3, 4, 5]))