import time
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed
from threading import currentThread


def thread_job(*args, **kwargs):
    time.sleep(2)
    print("current thread —— pid:{},thread id:{}".format(os.getpid(), currentThread().ident))
    print("thread finished: {}".format(kwargs.get("name")))
    return args[0]


def process_job(*args, **kwargs):
    time.sleep(2)
    thread_executor = ThreadPoolExecutor(max_workers=10)
    tasks = [
        thread_executor.submit(thread_job, *("var_" + str(idx),), **{"name": "thread_{}".format(idx)})
        for idx in range(2)]
    wait(tasks, return_when=ALL_COMPLETED)
    result = [task.result() for task in tasks]
    print("thread results: {}".format(result))
    print("current process —— pid:{},thread id:{}".format(os.getpid(), currentThread().ident))
    print("process finished: {}".format(kwargs.get("name")))
    return args[0]


if __name__ == "__main__":
    start_time = time.time()
    process_executor = ProcessPoolExecutor(max_workers=5)
    all_process = [process_executor.submit(process_job, *("variable_{}".format(idx),),
                                           **{"name": "process_{}".format(idx)}) for idx in range(2)]
    results = [each.result() for each in as_completed(all_process)]
    print("process results: {}".format(results))
    print("total cost {} seconds".format(time.time() - start_time))
