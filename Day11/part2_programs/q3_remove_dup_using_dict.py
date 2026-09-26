def remove_dup_dict(lst):
    return list(dict.fromkeys(lst))
print(remove_dup_dict([1,2,2,3,4,4,5]))