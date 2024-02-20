# 13) Write a Python program to check if a string contains only digits.("12345" -->True)


def has_only_digits(string):
    return string.isdigit()

string = input("Enter a string: ")
print(has_only_digits(string))
