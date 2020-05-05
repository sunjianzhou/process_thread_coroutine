import asyncio
import time


async def coroutine_job(value):
    print("start coroutine_job: {}".format(value))
    await asyncio.sleep(2)  # 不能使用time.sleep(),这样的话是同步，就不是异步；await就相当于yield from
    print("coroutine_job finished: {}".format(value))


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [coroutine_job(idx) for idx in range(3)]

    loop.run_until_complete(asyncio.wait(tasks))
    print("total cost {} seconds".format(time.time() - start_time))
