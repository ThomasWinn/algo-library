def binary_search(arr: list, target: int) -> bool:
    """
    Time: O(log(n))
    Space: O(1)

    Notes:
    On a sorted list, split the list in two halves comparing which side the target will be on

    need l <= r because the target might be where l == r - especially when array has one element

    need mid - 1 and mid + 1 parts otherwise infinite loop will happen 
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return False



t = sorted([34,67,234,678,1234,22,324,56])
print(t)

print(binary_search(t, 22))