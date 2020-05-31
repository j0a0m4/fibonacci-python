import time


def testFibo(fn, n):
    print('Calculating time diff for fn \n')
    for i in range(n):
        start = time.time()
        res = fn(i)
        end = time.time()
        print("n = {}, fibo = {}, tempo = {}".format(i, res, end - start))
        print("-" * 50)
