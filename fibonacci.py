def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    amount = int(input("Amount of numbers to print: "))
    n = 1
    while n <= amount:
        print(fibonacci(n))
        n += 1


if __name__ == '__main__':
    main()
