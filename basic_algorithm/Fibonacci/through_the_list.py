def fib(n):
    s = [0, 1]
    if n in [0, 1]:
        return n
    for i in range(1, n):
        s.append(s[-1]+s[-2])
    c = s.pop()
    return c

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
