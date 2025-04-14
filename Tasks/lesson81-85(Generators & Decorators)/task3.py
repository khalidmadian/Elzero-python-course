# speed test decoration task

from time import time


def my_decorator(func):
    def nested_func():
        start = time()
        func()
        end = time()

        print(f'the time for execution is {end - start}')

    return nested_func


@my_decorator
def print_numbers():
    for i in range(1, 20000):
        print(i)


print_numbers()