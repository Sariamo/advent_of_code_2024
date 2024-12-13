import itertools


def solve(val, eq, sol):
    res = int(val[0])
    val = val[1:]
    for i, v in enumerate(val):
        if eq[i] == "+":
            res += int(v)
        if eq[i] == "*":
            res *= int(v)
        if eq[i] == "|":
            res = int(str(res) + str(v))
    return res == int(sol)


equations = []
with open("input", "r") as inp:
    for equation in inp:
        equations.append(equation.replace(":", "").replace("\n", "").split(" "))

ctr = 0
try_ctr = 0
for eq in equations:
    sol = eq[0]
    parts = eq[1:]
    eq_pos = []
    tokens = ["+", "*", "|"]
    token_pos = [p for p in itertools.product(tokens, repeat=len(parts) - 1)]
    for token_perm in token_pos:
        if solve(parts, token_perm, sol):
            ctr += int(sol)
            break
    try_ctr += 1
    print(str(try_ctr) + "/" + str(len(equations)) + " done. ctr=" + str(ctr))

print(ctr)
