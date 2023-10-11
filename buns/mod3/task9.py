position = [0, 0]
x_shift = 1
y_shift = 1
x_direct = -1
y_direct = -1

with open("input.txt") as file:
    n = int(file.read())
    file.close()
#n = int(input())

def move(axis, m):
    if axis == 'x':
        counter = 0
        while m > 0 and counter != x_shift:
            position[0] += x_direct
            counter += 1
            m -= 1
    if axis == 'y':
        counter = 0
        while m > 0 and counter != y_shift:
            position[1] += y_direct
            counter += 1
            m -= 1


while n > 0:
    move('x', n)
    n -= x_shift
    x_shift += 1
    x_direct *= -1
    move('y', n)
    n -= y_shift
    y_shift += 1
    y_direct *= -1

with open('output.txt', 'w') as file:
    file.write(" ".join(map(str, position)))
    file.close()
#print(*position)




