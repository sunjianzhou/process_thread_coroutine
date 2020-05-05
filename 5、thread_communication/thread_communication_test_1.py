import time
import threading
import numpy as np

products = list()
producer_life = 3


def producer(num):
    global producer_life
    while True:
        cond.acquire()
        if len(products) == 0 and producer_life > 0:
            for _ in range(num):
                random_int = np.random.randint(100)
                print("producer a number: {}".format(random_int))
                products.append(random_int)
            cond.notifyAll()
            cond.release()
            producer_life -= 1
        elif producer_life > 0:
            cond.release()
        else:
            cond.release()
            break


def consumer(name):
    global producer_life
    while True:
        cond.acquire()
        if producer_life == 0:
            cond.release()
            return
        while len(products) == 0:
            cond.wait()
        print("{} consumer data: {}".format(name, products.pop()))
        cond.notifyAll()
        cond.release()
        time.sleep(0.5)


if __name__ == "__main__":
    cond = threading.Condition()
    thread_consumer_1 = threading.Thread(target=consumer, args=("consumer one",))
    thread_consumer_2 = threading.Thread(target=consumer, args=("consumer two",))
    thread_consumer_1.start()
    thread_consumer_2.start()
    thread_producer = threading.Thread(target=producer, args=(3,))
    thread_producer.start()
    thread_producer.join()
    thread_consumer_1.join()
    thread_consumer_2.join()
    print("main finished")
