from multiprocessing import Process, current_process, Semaphore
import time


def process_job(resource):
    resource.acquire()
    print("current process name: {}".format(current_process().name))
    time.sleep(2)
    resource.release()
    print("resource {} release".format(current_process().name))


if __name__ == '__main__':
    start_time = time.time()
    signal = Semaphore(2)
    process_jobs = list()
    for idx in range(4):
        process = Process(target=process_job, args=(signal,), name="process_{}".format(idx))
        process.daemon = True
        process_jobs.append(process)
    for each in process_jobs:
        each.start()
    for each in process_jobs:
        each.join()
    print("total cost {} seconds".format(time.time() - start_time))