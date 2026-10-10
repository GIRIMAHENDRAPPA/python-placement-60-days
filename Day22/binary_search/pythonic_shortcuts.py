import bisect

arr = [1, 2, 4, 7, 9, 11]

# 1. Find index using bisect
idx = bisect.bisect_left(arr, 7) # O(log n)

# 2. Check exists
# target in arr -> O(n) for list! Don't use for large sorted data