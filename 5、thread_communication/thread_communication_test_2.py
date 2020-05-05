import time
import threading


class MyClass:
    __instance = None
    __instance_lock = threading.Lock()

    def __init__(self):
        self._money = 0

    def get_money(self):
        return self._money

    def add_money(self, income):
        self._money += income

    @staticmethod
    def get_instance():
        if not MyClass.__instance:
            with MyClass.__instance_lock:
                if not MyClass.__instance:
                    MyClass.__instance = MyClass()
        return MyClass.__instance


def add_money(income, sleep_time=None, thread_name=None):
    print("{} begin".format(thread_name))
    time.sleep(sleep_time)
    global_ins.add_money(income)
    print("{} finished".format(thread_name))


if __name__ == "__main__":
    global_ins = MyClass.get_instance()
    threads = [threading.Thread(target=add_money,
                                args=(1000, 0.5 - idx * 0.1, "thread_{}".format(idx))) for idx in range(3)]
    for each_thread in threads:
        each_thread.start()
    for each_thread in threads:
        each_thread.join()
    print(global_ins.get_money())
    print("main finished")
