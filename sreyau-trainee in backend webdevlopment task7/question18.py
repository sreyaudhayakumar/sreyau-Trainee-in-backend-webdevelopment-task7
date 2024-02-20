# 18) Write a Python program to find the second largest number in a list.

list =[int(x) for x in input("Enter elements of the list separated by space: ").split()]
print("list of item",list)

list_sorted=sorted(list)
print("sorted list is",list_sorted)

if len(list_sorted) >= 2:
    second_largest = list_sorted[-2]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain enough elements to find the second largest number.")