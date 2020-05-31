def fibo4(n):
    f1 = 0
    f2 = 1
    return fibo(f1, f2, n)


def fibo(f1, f2, n):
    if n == 0:
        return f1
    else:
        n = n - 1
        return fibo(f2, (f1 + f2), n)
