# 24) Write a Python program to calculate the sum of all elements in a list recursively

def sum_list(list):
    if not list:
        return 0
    else:
        return list[0] + sum_list(list[1:])


user_input = input("Enter the elements of the list separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

total_sum = sum_list(numbers)

print("Sum of all elements in the list:", total_sum)
