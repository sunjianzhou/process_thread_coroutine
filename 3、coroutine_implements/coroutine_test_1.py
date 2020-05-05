def data_average():
    num, total = 0, 0
    count = 0
    average = total / count if count != 0 else 0
    while True:
        current_num = yield average
        total += current_num
        count += 1
        average = total / count if count != 0 else 0
        print("the current average number is: {}".format(average))


if __name__ == "__main__":
    data = data_average()
    next(data)
    data.send(10)
    data.send(20)
    data.send(30)
