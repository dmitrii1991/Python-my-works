cache = {}

def fib(x):
    assert x >= 0
    if x not in cache:
        cache[x] = x if x<=1 else fib(x - 1) + fib(x - 2)
    return cache[x]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
