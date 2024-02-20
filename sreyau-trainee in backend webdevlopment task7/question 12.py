# 12) Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])

# Define the flatten_list function
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [1, [2, 3], [4, [5, 6]]]
flattened_list = flatten_list(nested_list)
print("list:",nested_list)
print("Flattened list:", flattened_list)
