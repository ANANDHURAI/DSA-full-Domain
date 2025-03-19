def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 2



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    return -1  # Return -1 if target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 2