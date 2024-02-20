# 6) Write a Python program to merge two sorted lists into a single sorted list

def merge_lists(arr1, arr2):
    merged = sorted(arr1 + arr2)
    return merged

arr1 = [int(x) for x in input("Enter elements of the first list separated by space: ").split()]
arr2 = [int(x) for x in input("Enter elements of the second list separated by space: ").split()]

print("Merged and sorted list:", merge_lists(arr1, arr2))
