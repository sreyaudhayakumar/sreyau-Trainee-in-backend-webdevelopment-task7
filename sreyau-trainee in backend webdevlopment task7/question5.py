# 5) Write a Python program to implement a stack using a list.(push and pop)

def push(stack, item):
    stack.append(item)
    print("After push:", stack)

def pop(stack):
    if not is_empty(stack):
        item = stack.pop()
        print("After pop:", stack)
        return item
    else:
        print("Stack is empty")
        return None

def is_empty(stack):
    return len(stack) == 0

stack = []

while True:
    choice = input("Enter 'push <element>' to push an element, 'pop' to pop an element, or 'quit' to exit: ")

    if choice.startswith("push"):
        elements = choice.split(' ', 1)
        if len(elements) == 2:
            push(stack, elements[1])
        else:
            print("Invalid input. Please enter 'push <element>'.")
    elif choice == "pop":
        popped = pop(stack)
        if popped:
            print("Popped element:", popped)
    elif choice == "quit":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 'push <element>', 'pop', or 'quit'.")
