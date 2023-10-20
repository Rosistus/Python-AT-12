a = int(input())
b = int(input())


def euclid(a, b):
    if a != 0 and b != 0:
        if a > b:
            return euclid(a % b, b)
        else:
            return euclid(a, b % a)
    else:
        return a+b


print(euclid(a, b))
