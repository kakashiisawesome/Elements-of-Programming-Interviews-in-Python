
def willReturnToStart(s):
    x_stack, y_stack = [], []

    for i in s:
        if i == 'L' or i == 'R':
            if len(x_stack) == 0 or i == x_stack[len(x_stack)-1]:
                x_stack.append(i)
            else:
                x_stack.pop()
        else:
            if len(y_stack) == 0 or i == y_stack[len(y_stack)-1]:
                y_stack.append(i)
            else:
                y_stack.pop()

    return len(x_stack) == 0 and len(y_stack) == 0


print(willReturnToStart('RUULLDRD'))
