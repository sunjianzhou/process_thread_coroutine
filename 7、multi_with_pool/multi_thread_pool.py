import time
import os
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from threading import currentThread


def thread_job(var):
    time.sleep(2)
    print("process id is {}, and thread name is: {}".format(os.getpid(), currentThread().getName()))
    return "thread_" + str(var)


if __name__ == "__main__":
    start_time = time.time()
    thread_executor = ThreadPoolExecutor(max_workers=20)
    thread_tasks = [thread_executor.submit(thread_job, var=idx) for idx in range(5)]
    # thread_executor.shutdown()    #关闭线程池入口，并等待池中所有任务完成
    wait(thread_tasks, return_when=ALL_COMPLETED)
    print("threads results: {}".format([each.result() for each in thread_tasks]))
    print("main process finished: {}".format(os.getpid()))
    print("total cost {} seconds".format(time.time() - start_time))
