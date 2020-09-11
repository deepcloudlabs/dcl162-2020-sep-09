from timeit import timeit

import numpy as np

my_arr = np.arange(10000000)
my_list = list(range(10000000))


def compute1():
    for _ in range(10): my_arr2 = my_arr * 2


def compute2():
    for _ in range(10): my_list2 = [x * 2 for x in my_list]


time = timeit(compute1, number=1)
print(time)

time = timeit(compute2, number=1)
print(time)
