from dataclasses import dataclass


import random


def spam(divideBy: int):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        return print('Error: Invalid argument: {}'.format(e))
    finally:
        return print("-- division finished --")


def main():
    for i in range(5):
        print(random.randint(1, 10))
    spam(0)


if __name__ == "__main__":
    main()
