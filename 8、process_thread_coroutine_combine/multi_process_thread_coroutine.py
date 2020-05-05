import gevent
from gevent import monkey

monkey.patch_all(thread=False)
import os
import time
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from threading import Thread, currentThread
from queue import Queue


def coroutine_job(arg):
    time.sleep(2)
    print("current coroutine —— thread_id:{}".format(currentThread().ident))
    return "coroutine_" + str(arg)


def thread_job(my_que):
    time.sleep(2)
    print("current thread —— pid:{},thread_id:{}".format(os.getpid(), currentThread().ident))
    coroutine_jobs = [gevent.spawn(coroutine_job, "var_{}".format(idx)) for idx in range(2)]
    gevent.joinall(coroutine_jobs)
    print("thread result:{}".format([each_job.value for each_job in coroutine_jobs]))
    print("thread finished: {}".format(currentThread().getName()))
    my_que.put(currentThread().getName())


def process_job(*args, **kwargs):
    time.sleep(2)
    com_que = Queue()
    thread_tasks = [Thread(target=thread_job, args=(com_que,), name="thread_{}".format(idx)) for idx in range(2)]
    for each_thread in thread_tasks:
        each_thread.start()
    for each_thread in thread_tasks:
        each_thread.join()
    thread_results = []
    while not com_que.empty():
        thread_results.append(com_que.get())
    print("thread results: {}".format(thread_results))
    print("process finished: {}".format(kwargs.get("name")))
    return "process_" + str(args[0])


if __name__ == "__main__":
    start_time = time.time()
    process_executor = ProcessPoolExecutor(max_workers=8)
    all_process = [process_executor.submit(process_job, *(idx,),
                                           **{"name": "process_{}".format(idx)}) for idx in range(2)]
    wait(all_process, return_when=ALL_COMPLETED)
    print("process results: {}".format([each.result() for each in all_process]))
    print("total cost {} seconds".format(time.time() - start_time))
