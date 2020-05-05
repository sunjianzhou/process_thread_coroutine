import threading
import os


def target_func(str_arg, val=None):
    cur_thread = threading.currentThread()
    print("sub thread id: {}, sub thread name: {}".format(cur_thread.ident, cur_thread.name))
    print("process id: {}".format(os.getpid()))
    print(str_arg)
    print("name: {}".format(val))


if __name__ == "__main__":
    my_thread = threading.Thread(target=target_func, name="thread_1",
                                 args=("arg_test",), kwargs={"val": 66})
    my_thread.start()
    my_thread.join()
    print("main thread id: {}".format(threading.currentThread().ident))
    print("main process id: {}".format(os.getpid()))
