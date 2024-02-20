# 19) Write a Python program to count the number of vowels in a string.


def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


string = input("Enter a string: ")
print("The number of vowels in the string is:", count_vowels(string))