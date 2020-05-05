from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, p_name, *args, **kwargs):
        super(MyProcess, self).__init__(name=p_name)
        print("args: {}".format(args))
        print("kwargs: {}".format(kwargs))

    def run(self):
        print("current process name is {}, pid is {}".format(self.name, os.getpid()))


if __name__ == "__main__":
    process_1 = MyProcess("process 1", *["a", "b"], **{"key_a": "value_a"})
    process_1.start()
    process_1.join()
    print("subprocess pid: {}".format(process_1.pid))
    print("current process pid is: {}".format(os.getpid()))
