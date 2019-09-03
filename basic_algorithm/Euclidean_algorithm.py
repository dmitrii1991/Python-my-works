def gcd(a, b):
    while True:
        if a > b:
            a = a % b
            if a == 0:
                return b
        else:
            b = b % a
            if b == 0:
                return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
