#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    try:
        amount = int(input("Amount of numbers to print: "))
    except ValueError:
        logging.error('\nWrong input!')
        return
    n = 1
    while n <= amount:
        logging.info(fibonacci(n))
        n += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.error('\nKeyboard Interruption occured!')
