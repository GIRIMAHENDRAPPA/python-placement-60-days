def first_occurrence(arr, target):
    low, high, ans = 0, len(arr)-1, -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            ans = mid
            high = mid -1 # keep going left
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return ans