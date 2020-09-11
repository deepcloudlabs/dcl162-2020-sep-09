import logging
import os
import threading
import time

print(f"# of logical processors: {os.cpu_count()}")

def task(name, delay):
    logging.info(f"Thread {name} has started...")
    count = 0  # stack
    while count < 3:
        time.sleep(delay)
        count += 1
        logging.info(f"Thread {name} is running for {count} time...")
    logging.info(f"Thread {name} has finished.")


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

t1 = threading.Thread(target=task, args=("Thread #1", 2))
t2 = threading.Thread(target=task, args=("Thread #2", 4))

t1.start()
t2.start()
t1.join()  # blocking....
logging.info("t1.join() returns!")
t2.join()  # blocking....
logging.info("t2.join() returns!")
logging.info("done.")
