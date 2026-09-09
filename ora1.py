from time import time
import random

def add(n: int) -> dict[str, float | int]:
    sum_ = 0
    time_start = time()
    for i in range(n + 1):
        sum_ += i

    time_end = time()

    delta = float(time_end - time_start)

    return dict({"sum": sum_, "time": delta})


def add_gauss(n: int) -> dict[int, float]:
    time_start = time()

    s = int((n * (n + 1)) / 2)

    time_end = time()

    delta = float(time_end - time_start)

    return dict({"sum": s, "time": delta})


def smallest(ls: list):
    sm = ls[0]

    for i in range(1, len(ls)):
        if ls[i] < sm:
            sm = ls[i]

    return sm


def biggest(ls: list):
    big = ls[0]

    for i in range(1, len(ls)):
        if ls[i] > big:
            big = ls[i]

    return big


def rec_min(ls_: list):
    if len(ls_) < 2:
        return ls_[0]

    return None


if __name__ == "__main__":
    # res1 = add(1_000)['time']
    # res2 = add(10_000)['time']

    res3 = add_gauss(1_000)['time']
    res4 = add_gauss(10 ** 30)['time']
    res5 = add_gauss(10 ** 50)['time']
    res6 = add_gauss(10 ** 100)['time']

    # print(res4, res5, res6, sep=' | ')

    ls = [it for it in random.sample(range(1_000, 10_000), 1000)]
    random.shuffle(ls)

    smallest = smallest(ls)
    print(smallest)

    biggest = biggest(ls)
    print(biggest)

    # todo: measure time for each iteration

    # if float(res2) == float(res1 * 2):
    #     print(res1, res2, sep=' | ')
    #     print(True)
    # else:
    #     print(res1, res2, sep=' | ')
    #     print(False)