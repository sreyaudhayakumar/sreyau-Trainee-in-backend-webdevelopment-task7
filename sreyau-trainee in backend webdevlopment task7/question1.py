# 1) write a single program to handle the following arithmetic operations for addition, subtraction,
# multiplication , division, floor division,modulus and Exponentiation.

user_input1=int(input("enter a value 1:"))
user_input2=int(input("enter a value 2:"))
operator=input("enter the operator(+,-,*,/,//,%,**)")

if operator == '+':
    print("addition of two values:",user_input1+user_input2)
    
elif operator == '-':
    print("subtraction of two values:",user_input1-user_input2)
    
elif operator == '*':
    print("multiplication of two values:",user_input1*user_input2)
    
elif operator == '/':
    print("division of two values:",user_input1/user_input2)
    
elif operator == '//':
    print("floor division of two operator ",user_input1//user_input2)
    
elif operator == '%':
    print("modulus of two operator is:",user_input1%user_input2)
    
elif operator == '**':
    print("expontiation of value is",user_input1**user_input2)
    
else:
    print("invalid operation")