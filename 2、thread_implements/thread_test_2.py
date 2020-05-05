import threading
import time


class ThreadJob(threading.Thread):
    def __init__(self, thread_name, *args, **kwargs):
        super(ThreadJob, self).__init__(name=thread_name)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        time.sleep(0.5)
        print(self.name)
        print("args: {}".format(self.args))
        print("kwargs: {}".format(self.kwargs))


if __name__ == "__main__":
    params, param_kv = ["var_a", "var_b"], {"key_a": "value_a"}
    my_thread = ThreadJob("thread_name", *params, **param_kv)
    my_thread.start()
    print("main function")
