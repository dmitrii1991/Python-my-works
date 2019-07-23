import random
a = [random.randint(0, 1000) for x in range(0, 10)]
print('the original non-sorted list\n', a, '\n')

def sort_list(arr):

    def find_smallest(arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr) - 1):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest, smallest_index

    new_arr = []
    for i in range(len(arr) - 1):
        smallest, i = find_smallest(arr)
        new_arr.append(smallest)
        arr.pop(i)
    return new_arr

print('sorted list')
print(sort_list(a))
