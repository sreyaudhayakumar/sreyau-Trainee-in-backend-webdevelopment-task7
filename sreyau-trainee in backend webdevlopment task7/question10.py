# 10) Write a Python program to remove duplicates from a list.

def remove_duplicates(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list

list = input("Enter elements of the list separated by space: ").split()
list = [int(x) for x in list]

new_lists = remove_duplicates(list)

print("List after removing duplicates:", new_lists)
