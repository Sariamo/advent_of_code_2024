mat = []
with open("input", "r") as inp:
    for line in inp:
        row = []
        for st in line:
            if st != "\n":
                row.append(st)
        mat.append(row)

xmas_ctr = 0
possible_xmas = ["MMSS", "SSMM", "SMSM", "MSMS"]
for r, row in enumerate(mat):
    for i, s in enumerate(row):
        if s == "A":
                try:
                    if 0 < r < len(mat) and 0 < i < len(mat[r]):
                        cross_neighbors = mat[r - 1][i - 1] + mat[r - 1][i + 1] + mat[r + 1][i - 1] + mat[r + 1][i + 1]
                        if cross_neighbors in possible_xmas:
                            xmas_ctr += 1
                except:
                    continue

print(xmas_ctr)
