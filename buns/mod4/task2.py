number = int(input())
power = int(input())


def rec(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return rec(a * a, n / 2)
    else:
        return a * rec(a, n - 1)


print(rec(number, power))
