# 9) Write a Python program to count the occurrences of an element in a list

def count_occurrences(list,list_count):
    count = 0
    for item in list:
        if item == list_count:
            count += 1
    return count


list = input("Enter elements of the list separated by space: ").split()
list = [int(x) for x in list]

list_count = int(input("Enter the target element: "))

occurrences = count_occurrences(list, list_count)

print(f"The element {list_count} occurs {occurrences} times in the list.")
