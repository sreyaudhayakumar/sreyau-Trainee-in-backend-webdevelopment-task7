# 25) Write a Python program to count the number of occurrences of each element in a tuple

def count_element_occurrences(input_tuple):
    
    element_counts = {}

    for element in input_tuple:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    return element_counts


input_string = input("Enter elements of the tuple separated by spaces: ")
input_tuple = tuple(input_string.split())

occurrences = count_element_occurrences(input_tuple)
print("Occurrences of each element in the tuple:")
for element, count in occurrences.items():
    print(f"{element}: {count}")
