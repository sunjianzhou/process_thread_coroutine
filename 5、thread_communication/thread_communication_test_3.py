import time
import threading
from queue import Queue


def producer(my_que, num):
    time.sleep(2)
    print("thread {} produce a num: {}".format(threading.currentThread().name, num))
    my_que.put(num)


def consumer(my_que):
    print("thread {} consumer a num: {}".format(threading.currentThread().name, my_que.get()))


if __name__ == "__main__":
    que_resource = Queue()
    thread_one = threading.Thread(target=consumer, args=(que_resource,), name="consumer_thread")
    thread_two = threading.Thread(target=producer, args=(que_resource, 66), name="producer_thread")
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    print("main finished")
