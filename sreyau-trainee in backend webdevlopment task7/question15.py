# 15) Write a Python program to check if a string is an anagram of another string.("listen", "silent)

def check_anagram(string1, string2):
    
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    
    return sorted(string1) == sorted(string2)

input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

if check_anagram(input_string1, input_string2):
    print(f"{input_string1} and {input_string2} are anagrams.")
else:
    print(f"{input_string1} and {input_string2} are not anagrams.")
