import gevent
from gevent import monkey
import time

monkey.patch_all(thread=False)


def coroutine_job_1(*args):
    print("coroutine_job_1 start with args: {}".format(args))
    gevent.sleep(2)
    print("coroutine_job_1 finished")


def coroutine_job_2(**kwargs):
    print("coroutine_job_2 start with kwargs: {}".format(kwargs))
    time.sleep(2)
    print("coroutine_job_2 finished")


if __name__ == "__main__":
    start_time = time.time()
    job_list = list()
    params = ["var_a", "var_b"]
    kv_params = {"key_a": "value_a"}
    job_list.append(gevent.spawn(coroutine_job_1, *params))
    job_list.append(gevent.spawn(coroutine_job_2, **kv_params))
    gevent.joinall(job_list)
    print("total cost {} seconds".format(time.time() - start_time))
