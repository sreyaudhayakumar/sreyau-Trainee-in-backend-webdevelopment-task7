# 2)Write a program to check the validity of a password. Primary conditions for password validation:
# - minimum 8 charecters
# - The alphabet must be between [a-z]
# - At least one alphabet should be of Upper Case [A-Z]
# - At least 1 number or digit between [0-9].
# - At least 1 character from [ _ or @ or $ ].
# Examples:
# Input : R@m@_f0rtu9e$
# Output : Valid Password
# Input : Rama_fortune$
# Output : Invalid Password
# Explanation: Number is missing
# Input : Rama#fortu9e
# Output : Invalid Password
# Explanation: Must consist from _ or @ or $

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(c.islower() for c in password):
        return "Password must contain at least one lowercase letter."

    if not any(c.isdigit() for c in password):
        return "Password must contain at least one digit."

    if not any(c in '_@$' for c in password):
        return "Password must contain at least one of the following characters: '_', '@', or '$'."

    return "Valid Password"

password = input("Enter a password: ")
result = validate_password(password)
print(result)
