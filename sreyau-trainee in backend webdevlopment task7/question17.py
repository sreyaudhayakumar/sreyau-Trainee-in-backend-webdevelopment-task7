# 17) Write a Python program to find the sum of all even numbers in a list.


lst = [int(x) for x in input("Enter elements of the list separated by space: ").split()]

even_sum = 0
even_list = []

for num in lst:
    if num % 2 == 0:
        even_sum += num
        even_list.append(num)
        
print("List of even numbers:", even_list)       
print("Sum of even numbers in the list:", even_sum)

    
