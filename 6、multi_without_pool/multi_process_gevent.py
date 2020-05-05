from gevent import monkey

monkey.patch_all()
import gevent
import time


def eat(food_name):
    print(food_name)
    time.sleep(2)
    return "eat"


def play(game):
    print(game)
    time.sleep(2)
    return "play"


if __name__ == "__main__":
    start_time = time.time()
    g1 = gevent.spawn(eat, "egg")
    g2 = gevent.spawn(play, "basketball")
    g1.join()
    g2.join()
    # 上述两句话等价于  gevent.joinall([g1,g2])
    print("g1 value: {}".format(g1.value))
    print("g2 value: {}".format(g2.value))
    print("cost {} seconds".format(time.time() - start_time))
    print("=" * 20)
    start_time = time.time()
    tasks = [gevent.spawn(eat, food) for food in ["egg", "fish", "meet"]]
    gevent.joinall(tasks)
    print("cost {} seconds".format(time.time() - start_time))
