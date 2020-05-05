from multiprocessing import Queue, Process
import numpy as np
import time


class Producer(Process):
    def __init__(self, name, com_que, num):
        super(Producer, self).__init__(name=name)
        self.com_que = com_que
        self.num = num

    def run(self):
        for _ in range(self.num):
            random_int = np.random.randint(10)
            print("producer a number: {}".format(random_int))
            self.com_que.put(random_int)
            time.sleep(0.5)


class Consumer(Process):
    def __init__(self, name, com_que, *args, **kwargs):
        super(Consumer, self).__init__(name=name)
        self.com_que = com_que

    def run(self):
        time.sleep(0.5)
        while not self.com_que.empty():
            print("consumer a number: {}".format(self.com_que.get()))
            time.sleep(0.5)


if __name__ == "__main__":
    my_que = Queue()
    process_1 = Producer(name="producer", com_que=my_que, num=3)
    process_2 = Consumer(name="consumer", com_que=my_que)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    print("main finished")
