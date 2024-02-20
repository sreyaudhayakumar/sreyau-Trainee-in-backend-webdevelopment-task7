# 22) Write a Python program to check if a given number is a perfect number

def is_perfect_number(number):
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum == number

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
