def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
