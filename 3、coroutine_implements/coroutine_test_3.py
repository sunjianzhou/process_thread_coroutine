from greenlet import greenlet


def coroutine_job_1(var):
    print("coroutine_job_1 start with variable: {}".format(var))
    gr2.switch(888)
    print("coroutine_job_1 finished with variable: {}".format(var))


def coroutine_job_2(var):
    print("coroutine_job_2 start with variable: {}".format(var))
    gr1.switch("bye, coroutine_job_1")
    print("coroutine_job_2 finished with variable: {}".format(var))


if __name__ == "__main__":
    gr1 = greenlet(coroutine_job_1)
    gr2 = greenlet(coroutine_job_2)
    gr1.switch(666)
    gr2.switch("bye, coroutine_job_2")
