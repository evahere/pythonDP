import time
from datetime import datetime

# 1 1 2 3 5 8 13 21 34
def fib_test1(k):
    assert k > 0, 'k必须大于0'
    if k in [1, 2]:
        return 1
    return fib_test1(k-1) + fib_test1(k-2)

# 1 1 2 3 5 8 13 21 34
def fib_test2(k):
    assert k > 0, 'k必须大于0'
    k1 = 1
    k2 = 1
    k3 = 0
    for i in range(0, k - 2):
        k3 = k1 + k2
        k1 = k2
        k2 = k3
    return k3

def fib_for1(k):
    for i in range(k, k + 7):
        print(fib_test1(i))
        start_time = time.time()
        fib_test1(i)
        print('用递归求第{}个斐波那契数的运行时间：{}'.format(i, time.time() - start_time))

def fib_for2(k):
    for i in range(k, k + 7):
        print(fib_test2(i))
        start_time = time.time()
        fib_test2(i)
        print('用非递归求第{}个斐波那契数的运行时间：{}'.format(i, time.time() - start_time))

if __name__ == "__main__":
    # fib_for1(30)
    fib_for2(30)

