def get_neighbors_of_same_token(mat, row, column):
    neighbors = []
    vecs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for vec in vecs:
        dir_r, dir_c = vec
        if 0 <= (row + dir_r) < len(mat) and 0 <= (column + dir_c) < len(mat[row]) and mat[row + dir_r][column + dir_c] == mat[row][column]:
            neighbors.append([row + dir_r, column + dir_c])
    return neighbors


def get_scope(mat, row, column):
    return 4 - len(get_neighbors_of_same_token(mat, row, column))


mat = []
with open("input", "r") as inp:
    for row in inp:
        mat_row = []
        for token in row:
            if token != "\n":
                mat_row.append(token)
        mat.append(mat_row)

area_amounts = []
area_scopes = []
used_mat = [[False for token in row] for row in mat]
for row in range(len(mat)):
    for column in range(len(mat[row])):
        if not used_mat[row][column]:
            used_mat[row][column] = True
            area_amount = 1
            area_scope = get_scope(mat, row, column)
            curr_area_old = [[row, column]]
            while len(curr_area_old) > 0:
                curr_area_new = []
                for area in curr_area_old:
                    area_row, area_column = area
                    neighbors = [[r, c] for (r, c) in get_neighbors_of_same_token(mat, area_row, area_column) if not used_mat[r][c]]
                    for r, c in neighbors:
                        used_mat[r][c] = True
                    area_amount += len(neighbors)
                    for n_r, n_c in neighbors:
                        area_scope += get_scope(mat, n_r, n_c)
                    curr_area_new.extend(neighbors)
                curr_area_old = curr_area_new

            area_amounts.append(area_amount)
            area_scopes.append(area_scope)

print(sum([area_amounts[i]*area_scopes[i] for i in range(len(area_amounts))]))
