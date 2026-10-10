def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 # go right
        else:
            high = mid - 1 # go left

    return -1

arr = [1, 2, 4, 7, 9, 11] # SORTED
print(binary_search(arr, 7)) # -> 3