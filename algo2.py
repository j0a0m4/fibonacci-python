def fibo2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 1
        b = 1
        aux = a + b
        for i in range(2, n):
            aux = a + b
            a = b
            b = aux
        return aux
