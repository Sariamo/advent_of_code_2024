import itertools

an_mat = []
with open("input", "r") as inp:
    for row in inp:
        an_line = []
        for a in row:
            if a != "\n":
                an_line.append(a)
        an_mat.append(an_line)

vr = [rp for rp in range(len(an_mat) // 2)]
vr += [-rp for rp in range(len(an_mat) // 2)]
vc = [cp for cp in range(len(an_mat[0]) // 2)]
vc += [-cp for cp in range(len(an_mat[0]) // 2)]
vecs = list(itertools.product(vr, vc))
for i in range(len(vecs)):
    vecs[i] = list(vecs[i])
vecs = [v for v in vecs if v != [0, 0]]

an_found_mat = [[False for _ in range(len(row))] for _ in range(len(an_mat))]
for row_index, row in enumerate(an_mat):
    for column_index, column in enumerate(row):
        for vec in vecs:
            vec = list(vec)
            ans = []
            while 0 <= (row_index + vec[0]) < len(an_mat) and 0 <= (column_index + vec[1]) < len(row):
                ans.append(an_mat[row_index + vec[0]][column_index + vec[1]])
                vec[0] *= 2
                vec[1] *= 2
                if len(ans) > 1:
                    for an_i, an in enumerate(ans):
                        if an_i != (an_i // 2) and an == ans[an_i // 2] and an != ".":
                            an_found_mat[row_index][column_index] = True
                            break

print([val for row in an_found_mat for val in row].count(True))
