field = []
field.append(input())
for _ in range(len(field[0])-1):
    field.append(input())


def win_check(string):
    if string == 'X'*len(field):
        print('X')
    if string == 'O'*len(field):
        print('O')


for i in range(len(field)):
    line = ""
    for j in range(len(field)):
        line += field[i][j]
    win_check(line)
for i in range(len(field)):
    line = ""
    for j in range(len(field)):
        line += field[j][i]
    win_check(line)
line1 = line2 = ""
for i in range(len(field)):
    for j in range(len(field)):
        if i == j:
            line1 += field[i][j]
        if i + j == len(field)-1:
            line2 += field[i][j]
win_check(line1)
win_check(line2)




