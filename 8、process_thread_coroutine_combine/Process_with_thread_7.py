import gevent
from gevent import monkey, pool

monkey.patch_all(thread=False)
import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
from threading import currentThread


def coroutine_job(arg):
    time.sleep(2)
    print("current coroutine —— thread_id:{}".format(currentThread().ident))
    return "coroutine_" + str(arg)


def thread_job(*args, **kwargs):
    time.sleep(2)
    print("current thread —— pid:{},thread_id:{}".format(os.getpid(), currentThread().ident))
    coroutine_pool = pool.Pool(size=10)
    coroutine_jobs = [coroutine_pool.spawn(coroutine_job, "var_{}".format(idx)) for idx in range(2)]
    gevent.joinall(coroutine_jobs)
    print("thread result:{}".format([each_job.value for each_job in coroutine_jobs]))
    print("thread finished: {}".format(kwargs.get("name")))
    return "thread_" + str(args[0])


def process_job(*args, **kwargs):
    time.sleep(2)
    thread_executor = ThreadPoolExecutor(max_workers=10)
    tasks = [
        thread_executor.submit(thread_job, *("var_" + str(idx),), **{"name": "thread_{}".format(idx)})
        for idx in range(2)]
    wait(tasks, return_when=ALL_COMPLETED)
    result = [task.result() for task in tasks]
    print("thread results: {}".format(result))
    print("process finished: {}".format(kwargs.get("name")))
    return "process_" + str(args[0])


if __name__ == "__main__":
    start_time = time.time()
    process_executor = ProcessPoolExecutor(max_workers=8)
    all_process = [process_executor.submit(process_job, *(idx,),
                                           **{"name": "process_{}".format(idx)}) for idx in range(2)]
    print("process results: {}".format([each.result() for each in as_completed(all_process)]))
    print("total cost {} seconds".format(time.time() - start_time))
