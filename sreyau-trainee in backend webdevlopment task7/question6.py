# 6) Write a Python program to implement a queue using a list.(enqueue and dequeue)


def enqueue(queue, item):
    queue.append(item)
    print("After enqueue:", queue)

def dequeue(queue):
    if not is_empty(queue):
        item = queue.pop(0)
        print("After dequeue:", queue)
        return item
    else:
        print("Queue is empty")
        return None

def is_empty(queue):
    return len(queue) == 0

queue = []

while True:
    choice = input("Enter 'enqueue <element>' to enqueue an element, 'dequeue' to dequeue an element, or 'quit' to exit: ")

    if choice.startswith("enqueue"):
        if len(choice.split()) == 2:
            element = choice.split()[1]
            enqueue(queue, element)
        else:
            print("Invalid input. Please enter 'enqueue <element>'.")
    elif choice == "dequeue":
        dequeued = dequeue(queue)
        if dequeued:
            print("Dequeued element:", dequeued)
    elif choice == "quit":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 'enqueue <element>', 'dequeue', or 'quit'.")
