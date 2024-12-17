mat = []
with open("input", "r") as inp:
    for row in inp:
        mat_row = []
        for column in row:
            if column != "\n":
                mat_row.append(int(column))
        mat.append(mat_row)
ctr = 0
vecs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for row in range(len(mat)):
    for column in range(len(mat[row])):
        if mat[row][column] == 0:
            searchNumber = 1
            cords = [[row, column]]
            done = False
            while not done:
                new_cords = []
                for cord in cords:
                    for vec in vecs:
                        curr_row, curr_column = cord[0] + vec[0], cord[1] + vec[1]
                        if 0 <= curr_row < len(mat) and 0 <= curr_column < len(mat[curr_row]) and mat[curr_row][curr_column] == searchNumber:
                            new_cords.append([curr_row, curr_column])

                if len(new_cords) > 0:
                    if searchNumber == 9:
                        done = True
                        ctr += len(new_cords)
                    else:
                        cords = new_cords
                        searchNumber += 1
                else:
                    break
print(ctr)
