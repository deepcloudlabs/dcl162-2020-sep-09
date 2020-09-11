from random import randint
from threading import Thread

lottery_numbers = []


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    lottery_numbers.append(numbers)


threads = []

for i in range(0, 10000):
    threads.append(Thread(target=draw_lottery_numbers, args=(49, 6)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"{len(lottery_numbers)}")
for numbers in lottery_numbers:
    print(numbers)
