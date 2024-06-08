# QUE7: BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def recursive_search(sorted_list, target, start, end):
    if start > end:
        return -1  # Target is not in the list

    mid = (start + end) // 2
    if sorted_list[mid] == target:
        return mid  # Target found
    elif sorted_list[mid] > target:
        return recursive_search(sorted_list, target, start, mid - 1)
    else:
        return recursive_search(sorted_list, target, mid + 1, end)


# Example usage
numbers = sorted([10, 5, 8, 12, 3, 7])  # sorted for binary search
target = int(input("Enter a number to search: "))
result = recursive_search(numbers, target, 0, len(numbers) - 1)
print(f"Number {target} found at index {result}" if result != -1 else f"Number {target} not found.")