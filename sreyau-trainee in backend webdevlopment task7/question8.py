# Write a Python program to reverse a list.
def reverse_list(list):
    list.reverse()

list = input("Enter elements of the list separated by space: ").split()
print("list befor sort",list)

list = [int(x) for x in list]

reverse_list(list)
print("list after sort",list) 
