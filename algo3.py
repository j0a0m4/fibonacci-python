def fibo3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo3(n - 1) + fibo3(n - 2)
