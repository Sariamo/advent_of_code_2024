import itertools

an_mat = []
with open("input", "r") as inp:
    for row in inp:
        an_line = []
        for a in row:
            if a != "\n":
                an_line.append(a)
        an_mat.append(an_line)

vr = [rp for rp in range(len(an_mat))]
vr += [-rp for rp in range(len(an_mat))]
vc = [cp for cp in range(len(an_mat[0]))]
vc += [-cp for cp in range(len(an_mat[0]))]
vecs = list(itertools.product(vr, vc))
for i in range(len(vecs)):
    vecs[i] = list(vecs[i])
vecs = [v for v in vecs if v != [0, 0]]

an_found_mat = [[False for _ in range(len(row))] for _ in range(len(an_mat))]
for row_index, row in enumerate(an_mat):
    for column_index, token in enumerate(row):
        for vec in vecs:
            vec = list(vec)
            if token != ".":
                ans = [token]
            else:
                ans = []
            org_vec = [vec[0], vec[1]]
            while 0 <= (row_index + vec[0]) < len(an_mat) and 0 <= (column_index + vec[1]) < len(row):
                next_token = an_mat[row_index + vec[0]][column_index + vec[1]]
                if next_token != ".":
                    ans.append(next_token)
                vec[0] += org_vec[0]
                vec[1] += org_vec[1]

            if len(ans) > 1:
                for an_i in range(len(ans)):
                    for an_j in range(len(ans)):
                        if an_i != an_j and ans[an_i] == ans[an_j] and ans[an_i] != ".":
                            an_found_mat[row_index][column_index] = True
                            break

print([val for row in an_found_mat for val in row].count(True))
