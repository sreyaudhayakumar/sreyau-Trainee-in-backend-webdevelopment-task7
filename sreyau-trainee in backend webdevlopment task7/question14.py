# 14) Write a Python program to check if a given year is a leap year

year=int(input("enter a year:"))

if (year%4 == 0 and year%100!=0) or (year%400 == 0):
    print(year,"is leap year")
else:
    print(year,"not leap year")