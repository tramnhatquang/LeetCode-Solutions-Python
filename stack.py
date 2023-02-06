# HELPER FUNCTION FOR CREATING AND MANIPULATING A STACK

def createStack():  # Function to create an empty stack
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):  # push item to stack
    stack.append(item)


def pop(stack):  # pop item from stack

    if (isEmpty(stack)):  # display error if stack empty
        print("Stack Underflow ")
        exit(1)

    return stack.pop()


def printStack(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
