from multiprocessing import Pool, Manager
import numpy as np
import time


def producer(com_que, num):
    for _ in range(num):
        random_int = np.random.randint(10)
        print("producer a number: {}".format(random_int))
        com_que.put(random_int)
        time.sleep(0.5)


def consumer(com_que):
    time.sleep(0.5)
    while not com_que.empty():
        print("consumer a number: {}".format(com_que.get()))
        time.sleep(0.5)


if __name__ == "__main__":
    my_que = Manager().Queue()
    pool = Pool(2)
    pool.apply_async(producer, args=(my_que, 3))
    pool.apply_async(consumer, args=(my_que,))
    pool.close()
    pool.join()

