import random
# make a random number
a = random.randint(0, 1000000)
list_a = [x for x in range(0, 1000000, 2)]

def binary_search(list_a, item):
    low = 0
    high = len(list_a) - 1
    k = 0

    while low <= high:
        k += 1
        mid = round((low + high) / 2)
        guess = list_a[mid]
        if guess == item:
            return f'We found this number{guess } in the list at the position {mid}, search steps6  {k}'
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return "NUMBER NOT IN LIST"


print(f'загадали число {a}')
print(binary_search(list_a, a), '\n')

print(f'загадали число {a+1}')
print(binary_search(list_a, a+1))
