robots = []
with open("input", "r") as inp:
    for line in inp:
        robots.append([int(x) for x in line.replace("v", "").replace(" ", ",").replace("p", "").replace("=", "").split(",")])

field_width = 101
field_height = 103
seconds = 1000
middle_row = field_height // 2
middle_column = field_width // 2

field = [[0 for _ in range(field_width)] for _ in range(field_height)]

for robot in robots:
    y, x, vy, vx = robot
    field[x][y] += 1
s = 1
chain_ctr_max_max = 0
while True:
    for index, robot in enumerate(robots):
        y, x, vy, vx = robot
        field[x][y] -= 1
        x = (x + vx) % field_height
        y = (y + vy) % field_width
        field[x][y] += 1
        robots[index] = [y, x, vy, vx]

    vecs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    chain_ctr_max = 0
    for row in range(0, len(field)):
        for column in range(len(field[row])):
            if field[row][column] == 1:
                curr_row = row
                curr_column = column
                chain_ctr = 0
                one_found = True
                hist = []
                while one_found:
                    one_found = False
                    for vec in vecs:
                        if 0 <= curr_row + vec[0] < len(field) and 0 <= curr_column + vec[1] < len(field[0]) and \
                                field[curr_row + vec[0]][curr_column + vec[1]] == 1 and [curr_row + vec[0], curr_column + vec[1]] not in hist:

                            chain_ctr += 1
                            curr_row += vec[0]
                            curr_column += vec[1]
                            one_found = True
                            hist.append([curr_row, curr_column])

                if chain_ctr_max < chain_ctr:
                    chain_ctr_max = chain_ctr
    if chain_ctr_max_max < chain_ctr_max:
        chain_ctr_max_max = chain_ctr_max
        print(s, chain_ctr_max_max)
        if s == 7584:
            for row in field:
                print(row)
    s += 1
