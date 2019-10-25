# -*- coding: utf-8 -*-

import time


def math_squares_of_odd(ls: list):
    return sum((elem ** 2 for elem in ls if elem % 2 == 1))

def benchmark(func):
    def wrapper(*args, **kwags):
        start_func = time.time_ns()
        try:
            func(*args, **kwags)
            end_func = time.time_ns()
            print('{} выполнила задачу за {} наносек.'.format(func.__name__, (end_func - start_func)))
        except:
            end_func = time.time_ns()
            print('{} невыполнила задачу и закрашилась за {} наносек.'.format(func.__name__, (end_func - start_func)))
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
