import gevent
from gevent import monkey

monkey.patch_all(thread=False)
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from threading import currentThread
import time
import os


def coroutine_job(arg=None):
    time.sleep(2)
    print("current coroutine —— process id: {} thread id:{}".format(os.getpid(), currentThread().ident))
    return "coroutine_" + str(arg)


def process_job(*args, **kwargs):
    time.sleep(2)
    print("current process —— pid:{},process_name:{}".format(os.getpid(), kwargs.get("name")))
    job_kwargs = [{"arg": idx} for idx in range(3)]
    coroutine_jobs = [gevent.spawn(coroutine_job, **each) for each in job_kwargs]
    gevent.joinall(coroutine_jobs)
    print("thread result:{}".format([each.value for each in coroutine_jobs]))
    return "process_" + str(args[0])


if __name__ == "__main__":
    start_time = time.time()
    process_executor = ProcessPoolExecutor(max_workers=8)
    all_process = [process_executor.submit(process_job, *(idx,),
                                           **{"name": "process_{}".format(idx)}) for idx in range(2)]
    wait(all_process, return_when=ALL_COMPLETED)
    results = [each.result() for each in all_process]
    print("process results: {}".format(results))
    print("total cost {} seconds".format(time.time() - start_time))
