import os
from concurrent.futures.thread import ThreadPoolExecutor
from random import randint

num_of_cpus = os.cpu_count()


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers


futures = []
lottery_numbers = []
with ThreadPoolExecutor(max_workers=num_of_cpus) as my_thread_pool:
    for i in range(0, 10000):
        future = my_thread_pool.submit(draw_lottery_numbers, 49, 6)
        futures.append(future)

for future in futures:
    lottery_numbers.append(future.result())

for numbers in lottery_numbers:
    print(numbers)
