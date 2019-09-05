def memo(f):
    cache = {}
    def inner(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return inner


@memo
def fib(x):
    assert x >= 0
    return x if x <= 1 else fib(x - 1) + fib(x - 2)


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
