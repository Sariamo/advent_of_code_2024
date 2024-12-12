field = []

with open("input", "r") as inp:
    for line in inp:
        row = []
        for token in line:
            if token != "\n":
                row.append(token)
        field.append(row)

i_min, j_min, i, j, i_max, j_max, start_i, start_j = 0, 0, 0, 0, len(field) - 1, len(field[0]) - 1, 0, 0

for row in range(i_max):
    for column in range(j_max):
        if field[row][column] == "^":
            start_i = row
            start_j = column

dir_order = ["up", "right", "down", "left"]
dir = dir_order[0]
dir_vec = [[-1, 0], [0, 1], [1, 0], [0, -1]]
loop_ctr = 0

for obs_row in range(len(field)):
    for obs_token in range(len(field[obs_row])):
        if field[obs_row][obs_token] == "#" or field[obs_row][obs_token] == "^":
            continue

        field[obs_row][obs_token] = "#"

        hist = []
        dir = dir_order[0]
        i, j = start_i, start_j
        while i_min < i < i_max and j_min < j < j_max:

            if [i, j, dir] in hist:
                loop_ctr += 1
                break
            else:
                hist.append([i, j, dir])

            dir_i, dir_j = dir_vec[dir_order.index(dir)]

            while field[i + dir_i][j + dir_j] == "#":
                dir = dir_order[(dir_order.index(dir) + 1) % 4]
                dir_i, dir_j = dir_vec[dir_order.index(dir)]

            i += dir_i
            j += dir_j

        field[obs_row][obs_token] = "."

print(loop_ctr)
