field = []
instructions = []
part_two = False
with open("input", "r") as inp:
    for line in inp:
        if "#" in line and not part_two:
            row = []
            for token in line:
                if token != "\n":
                    row.append(token)
            field.append(row)
        else:
            part_two = True
            for token in line:
                if token != "\n":
                    instructions.append(token)
vecs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
instruction_tokens = ['>', 'v', '<', '^']
pos = []
for row in range(len(field)):
    for column in range(len(field[row])):
        if field[row][column] == "@":
            pos = [row, column]
s = 0

start_pos = [0, 0]
for inst in instructions:

    vec = vecs[instruction_tokens.index(inst)]
    iter_num = 0
    start_pos[0] = pos[0]
    start_pos[1] = pos[1]
    while True:
        pos[0] += vec[0]
        pos[1] += vec[1]
        iter_num += 1
        if not (0 <= pos[0] < len(field) and 0 <= pos[1] < len(field[0])):
            pos[0] = start_pos[0]
            pos[1] = start_pos[1]
            break
        if field[pos[0]][pos[1]] == "#":
            pos[0] = start_pos[0]
            pos[1] = start_pos[1]
            break
        elif field[pos[0]][pos[1]] == ".":
            for _ in range(iter_num):
                prev_pos_x = pos[0]
                prev_pos_y = pos[1]
                pos[0] -= vec[0]
                pos[1] -= vec[1]
                field[prev_pos_x][prev_pos_y] = field[pos[0]][pos[1]]
                field[pos[0]][pos[1]] = "."
            pos[0] = start_pos[0]
            pos[1] = start_pos[1]
            pos[0] += vec[0]
            pos[1] += vec[1]
            break

for row in field:
    print("".join(row))

for row in range(len(field)):
    for column in range(len(field[row])):
        if field[row][column] == "O":
            s += row * 100 + column

print(s)