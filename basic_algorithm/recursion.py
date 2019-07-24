# Basic examples
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

countdown(10)

#Call stack with recursion

def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i-1)

print(factorial(10))
