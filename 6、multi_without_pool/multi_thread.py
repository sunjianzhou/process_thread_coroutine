import threading
import time


def my_start():
    print("thread {} start".format(threading.currentThread().name))
    var = 0
    time.sleep(2)
    for num in range(100 * 100):
        var += num


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for idx in range(5):
        t = threading.Thread(target=my_start, name='thread_{}'.format(idx))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Main thread cost time: %s" % (time.time() - start_time))
