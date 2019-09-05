def fib(n):
    f0, f1 = 0, 1
    for i in range(1, n):
        f0, f1 = f1, f0 + f1
    return f1

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
