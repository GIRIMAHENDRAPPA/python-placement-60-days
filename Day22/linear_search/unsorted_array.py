def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
arr = [4,2,9,1,7]
print(linear_search(arr,9))