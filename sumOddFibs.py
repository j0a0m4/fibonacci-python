# Calculates the sum of all odd Fibonacci numbers that are less than or equal to num.
def sumOddFibs(num):
    sum = 0
    i = 0
    while sum <= num:
        res = fibo(i)
        i = i + 1
        if (res > num):
            break
        if (isOdd(res)):
            sum = sum + res
    return sum


# Finds nth fibonnaci number usign recursion
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# Checks if num is odd
def isOdd(num):
    return num % 2 != 0


# Testing for values
test = {
    4: 5,
    75024: 60696,
    75025: 135721,
    1000: 1785,
    4000000: 4613732,
}

for key, value in test.items():
    res = sumOddFibs(key)
    assert res == value, f"fibo({key}) should equal {value}"
    print(f"fibo({key}) - Test Passed!")
    print(f"{key} -> {value} === {res} \n")
