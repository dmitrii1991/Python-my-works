# -*- coding: utf-8 -*-

import time


def math_squares_of_odd(ls: list):
    return sum([i ** 2 for i in ls if i % 2 == 1])

def benchmark(func):
    def wrapper(*args, **kwags):
        start_func = time.time()
        func(*args, **kwags)
        end_func = time.time()
        print('{} выполнила задачу за {} сек.'.format(func.__name__, round(end_func - start_func, 2)))
    return wrapper

def palindrome(word: str):
    word_list = list(word)
    word_set = set(word)
    letter_without_pair = 0
    for letter in word_set:
        if word_list.count(letter) % 2 != 0:
            if letter_without_pair != 0:
                return False
            letter_without_pair += 1
    return True

@benchmark
def doo(x):
    k = 0
    for i in range(x):
        k += i

if __name__ == '__main__':
    doo(10000000)
