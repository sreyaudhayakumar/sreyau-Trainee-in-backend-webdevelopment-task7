# 11) Write a Python program to find the intersection of two lists

list1 = input("Enter elements of the first list separated by space: ").split()
list1 = [int(x) for x in list1]

list2 = input("Enter elements of the second list separated by space: ").split()
list2 = [int(x) for x in list2]

intersect = list(set(list1) & set(list2))

if intersect:
    print("Intersection of the two lists:", intersect)
else:
    print("Intersection of the two lists: no element is common")
