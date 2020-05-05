import time
import gevent
from gevent import monkey, pool
from threading import currentThread

monkey.patch_all(thread=False)


def coroutine_job(arg=None):
    time.sleep(2)
    print("current coroutine —— thread_id:{}".format(currentThread().ident))
    print("coroutine args: {}".format(arg))
    return "coroutine_" + str(arg)


if __name__ == "__main__":
    start_time = time.time()
    coroutine_pool = pool.Pool(size=2)
    job_kwargs = [{"arg": idx} for idx in range(4)]
    coroutine_jobs = [coroutine_pool.spawn(coroutine_job, **each) for each in job_kwargs]
    gevent.joinall(coroutine_jobs)
    print("coroutine results:{}".format([each.value for each in coroutine_jobs]))
    print("total cost {} seconds".format(time.time() - start_time))
    print("main thread finished: {}".format(currentThread().ident))
