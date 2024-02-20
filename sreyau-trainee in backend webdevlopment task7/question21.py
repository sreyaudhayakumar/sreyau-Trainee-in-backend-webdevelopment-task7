# 21) Write a Python program to remove all whitespace characters from a string

def remove_whitespace(string):
    return string.replace(" ","")

string=str(input("enter the string:"))

result_string=remove_whitespace(string)
print("string:",string)
print("string after remove all whitespace characters is:",result_string)

