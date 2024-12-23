robots = []
with open("input", "r") as inp:
    for line in inp:
        robots.append([int(x) for x in line.replace("v", "").replace(" ", ",").replace("p", "").replace("=", "").split(",")])

field_width = 101
field_height = 103
seconds = 100

field = [[0 for _ in range(field_width)] for _ in range(field_height)]
for robot in robots:
    y, x, vy, vx = robot
    field[x][y] += 1
    cpx = x
    cpy = y
    for _ in range(seconds):
        field[cpx][cpy] -= 1
        cpx = (cpx + vx) % field_height
        cpy = (cpy + vy) % field_width
        field[cpx][cpy] += 1

middle_row = field_height // 2
middle_column = field_width // 2

product = 1
factor = 0
for row in range(0, middle_row):
    for column in range(0, middle_column):
        factor += field[row][column]
product *= factor
factor = 0
for row in range(middle_row + 1, len(field)):
    for column in range(0, middle_column):
        factor += field[row][column]
product *= factor
factor = 0
for row in range(0, middle_row):
    for column in range(middle_column + 1, len(field[0])):
        factor += field[row][column]
product *= factor
factor = 0
for row in range(middle_row + 1, len(field)):
    for column in range(middle_column + 1, len(field[0])):
        factor += field[row][column]
product *= factor

print(product)