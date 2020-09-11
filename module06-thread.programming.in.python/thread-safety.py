import os
from threading import Thread, Lock

counter = 0
v = Lock()


def task(name):
    global counter
    with v:
        print(f"Thread {name} is running...")
        for i in range(0, 500000):
                counter += 1
        print(f"Thread {name} is exiting...")


threads = []

for i in range(0, os.cpu_count()):
    t = Thread(target=task, args=(f"#{i + 1}",))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(f"counter: {counter}")
