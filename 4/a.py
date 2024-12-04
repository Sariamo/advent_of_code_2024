mat = []
with open("input", "r") as inp:
    for line in inp:
        row = []
        for st in line:
            if st != "\n":
                row.append(st)
        mat.append(row)

xmas_ctr = 0
dirs = [[0, 1], [1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1], [-1, 0], [0, -1]]
for r, row in enumerate(mat):
    for i, s in enumerate(row):
        if s == "X":
            for dir in dirs:
                x, y = dir
                try:
                    if 0 <= (r + 3*x) <= (len(mat) - 1) and 0 <= (i + 3*y) <= (len(mat[x]) - 1) and mat[r + x][i + y] == "M" and mat[r + 2*x][i + 2*y] == "A" and mat[r + 3*x][i + 3*y] == "S":
                        xmas_ctr += 1
                except:
                    continue

print(xmas_ctr)

