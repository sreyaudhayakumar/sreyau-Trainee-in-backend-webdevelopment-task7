# 23) Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 
# 60)=12)

def Greatest_Common_Divisor(a, b):
    if b == 0:
        return a
    else:
        return Greatest_Common_Divisor(b, a % b)


a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))


result = Greatest_Common_Divisor(a, b)

print("Greatest_Common_Divisor of", a, "and", b, "=", result)
