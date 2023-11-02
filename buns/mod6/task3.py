def armstrong_numbers():
    num = 1

    while True:
        num_str = str(num)
        num_sum = sum((int(i)) ** len(num_str) for i in num_str)
        if num_sum == num and num not in range(0, 10):
            yield num
        num += 1


generator = armstrong_numbers()


def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
