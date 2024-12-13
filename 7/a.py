def dec_to_bin(dec, l):
    binary = bin(dec)[2:]
    while len(binary) < l:
        binary = "0" + binary
    return binary


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

for eq in equations:
    sol = eq[0]
    parts = eq[1:]

    eq_pos = []
    tokens = ["+", "*"]
    for i in range(2**(len(parts))):
        token_bin = dec_to_bin(i, len(parts))
        eq_i = ""
        for j in range(len(parts)):
            eq_i += tokens[int(token_bin[j])]
        if solve(parts, eq_i, sol):
            ctr += int(sol)
            break

print(ctr)

