import time
import os
from concurrent.futures import ProcessPoolExecutor, as_completed, wait, ALL_COMPLETED


def process_job(var):
    time.sleep(2)
    print("process id: {}, parent process id: {}".format(os.getpid(), os.getppid()))
    print("process {} finish".format(os.getpid()))
    return "process_" + str(var)


if __name__ == "__main__":
    start_time = time.time()
    process_executor = ProcessPoolExecutor(max_workers=5)
    process_tasks = [process_executor.submit(fn=process_job, var=variable)
                     for variable in range(3)]
    # process_executor.shutdown()
    # print("results are: {}".format([each.result() for each in as_completed(process_tasks)]))
    wait(process_tasks, return_when=ALL_COMPLETED)
    print("results are: {}".format([task.result() for task in process_tasks]))
    print("total cost {} seconds".format(time.time() - start_time))
    print("main process finished: {}".format(os.getpid()))
