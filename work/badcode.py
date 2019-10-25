# -*- coding: utf-8 -*-

def fun_func_with_correct(data):
    """optimized and fixed code"""
    if data:
        if (len(set([int(i) for i in data])) == 1) or \
                ([int(i)+1 for i in data[:-1]] == [int(i) for i in data[1:]]) or \
                ([int(i) for i in data[-2::-1]] == [int(i) + 1 for i in data[:0:-1]]):
            return True
        return False
    raise ValueError("data is None"))

def fun_func_without_correct(data):
    """optimized code"""
    if data:
        if 0 not in set(data):
            if len(set(data)) == 1:
                return 1
            if [int(i)+1 for i in data[:-1]] == [int(i) for i in data[1:]]:
                return 1
            if [int(i) for i in data[-2::-1]] == [int(i) + 1 for i in data[:0:-1]]:
                return 1
    else:
        raise ValueError("data is None")

def isFunnyFunction(data: list):
    if data != None:
        i = data[0]
        for j in range(1, len(data)):
            if data[j] != i:
                i = 0
                break
        if i == 0:
            i = int(data[0])
            for j in range(1, len(data)):
                if int(data[j]) == i + 1:
                    i += 1
                else:
                    i = 0
                    break
            if i != 0:
                return 1
        else:
            return 1
        i = int(data[len(data) - 1])
        for j in range(len(data) - 2, -1, -1):
            if int(data[j]) != i + 1:
                i = 0
                break
            else:
                i += 1
        if i != 0:
            return 1
    else:
        raise ValueError("data is None")


if __name__ == '__main__':
    pass
