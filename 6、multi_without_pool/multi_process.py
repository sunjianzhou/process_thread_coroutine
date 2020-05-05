from multiprocessing import Process
import time


def process_job(process_name):
    print("process {} start".format(process_name))
    var = 0
    time.sleep(2)
    for num in range(100 * 100):
        var += num


if __name__ == '__main__':
    start_time = time.time()
    my_process = []
    for idx in range(5):
        each = Process(target=process_job, args=('process_{}'.format(idx),))
        my_process.append(each)
    for each in my_process:
        each.start()
    for each in my_process:
        each.join()
    print("Main thread cost time: %s" % (time.time() - start_time))
