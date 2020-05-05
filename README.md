# process_thread_coroutine

---
## 理论相关内容，欢迎关注微信公众号：数据分析师成长之路

---
# 本篇大纲

## 1、python实现进程的两种方式
    1、实例化一个multiprocessing.Process的对象，并传入目标函数和参数。
    2、继承multiprocessing.Process，并重写run函数。
## 2、python实现线程的两种方式
    1、实例化一个threading.Thread的对象，并传入目标函数和参数。
    2、继承threading.Thread，并重写run函数。
## 3、python实现协程的四种方式
    1、使用yield实现。
    2、使用asyncio配合await来实现。
    3、使用greenlet模块来实现。
    4、使用gevent模块来实现。
## 4、进程通信的四种方式
    1、管道
    2、信号量
    3、消息队列
    4、共享内存
## 5、线程安全的三种线程通信方式
    1、多线程访问全局变量，加锁来避免线程安全问题。
    2、多线程访问某个实例，该实例是一个线程安全的单例模式。
    3、使用一些线程安全的数据结构。比如queue.Queue()。
## 6、多进程、多线程、多协程非池子方式的实现
    1、非进程池的方式实现多进程。主要使用multiprocessing.Process()
    2、非线程池方式实现多线程。主要使用threading.Thread()
    3、非协程池方式实现多协程，主要使用gevent
## 7、多进程、多线程、多协程池子方式的实现
    1、使用进程池实现多进程。主要使用concurrent.futures.ProcessPoolExecutor
    2、使用线程池实现多线程。主要使用concurrent.futures.ThreadPoolExecutor
    3、使用协程池实现多协程。主要使用gevent.pool
## 8、高并发杀手锏：多进程、多线程、多协程的配合使用
    1、多进程 + 多线程
    主要使用concurrent.futures的ProcessPoolExecutor和ThreadPoolExecutor
    2、多进程 + 多协程
    主要使用concurrent.futures.ProcessPoolExecutor和gevent
    3、多进程 + 多线程 + 多协程
    主要使用concurrent.futures的ProcessPoolExecutor和ThreadPoolExecutor，以及gevent.pool
    4、多进程 + 多线程 + 多协程
    主要使用concurrent.futures的ProcessPoolExecutor和threading.Thread，以及gevent