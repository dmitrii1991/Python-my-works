def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
