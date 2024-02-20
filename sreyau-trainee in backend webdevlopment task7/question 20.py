# 20) Write a Python program to remove all occurrences of a given element from a list.

def remove_occurrences(list, element):
    while element in list:
        list.remove(element)
    return list

user_input_list = input("Enter the list elements separated by spaces: ").split()
user_input_list = [int(x) for x in user_input_list]

element_remove = int(input("Enter the element to remove: "))
new_list = remove_occurrences(user_input_list, element_remove)

print("Original list:", user_input_list)
print("List after removing all occurrences of", element_remove, ":", new_list)
