def rotate(arr, k):
    k = k % len(arr)  # Handle cases where k is greater than the length of the array
    return arr[-k:] + arr[:-k]

print(rotate([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]