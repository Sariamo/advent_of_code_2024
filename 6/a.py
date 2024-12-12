field = []

with open("input", "r") as inp:
    for line in inp:
        row = []
        for token in line:
            if token != "\n":
                row.append(token)
        field.append(row)

i_min = 0
j_min = 0

i_max = len(field) - 1
j_max = len(field[0]) - 1

i = 0
j = 0

for row in range(i_max):
    for column in range(j_max):
        if field[row][column] == "^":
            i = row
            j = column

dir_order = ["up", "right", "down", "left"]
dir = dir_order[0]
dir_vec = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while i_min < i < i_max and j_min < j < j_max:
    dir_i, dir_j = dir_vec[dir_order.index(dir)]
    if field[i + dir_i][j + dir_j] == "#":
        dir = dir_order[(dir_order.index(dir) + 1) % 4]
        dir_i, dir_j = dir_vec[dir_order.index(dir)]
    field[i][j] = "X"
    i += dir_i
    j += dir_j

field[i][j] = "X"

print([token == "X" for r in field for token in r].count(True))
