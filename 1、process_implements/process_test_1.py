from multiprocessing import Process
import os


def my_func(*params, **kwargs):
    print("params value : {}, kwargs value: {}".format(params, kwargs))
    print("current process pid: {}".format(os.getpid()))


if __name__ == "__main__":
    sub_proc = Process(target=my_func, args=("param_value",), kwargs={"key_a": "value_a"}, name="name_1")
    sub_proc.start()
    sub_proc.join()
    print("subprocess pid: {}".format(sub_proc.pid))
    print("subprocess name: {}".format(sub_proc.name))
    print("main process pid: {}".format(os.getpid()))