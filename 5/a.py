r = []
o = []
part_two = False
with open("input", "r") as inp:
    for line in inp:
        if line == "" or line == "\n":
            part_two = True
            continue
        if not part_two:
            r.append([l.replace("\n", "") for l in line.split("|")])
        else:
            o.append([l.replace("\n", "") for l in line.split(",")])

ctr = 0
for order in o:
    valid = True
    for i, num in enumerate(order):
        num = int(num)
        for rule in r:
            first, second = [int(ru) for ru in rule]

            # before
            if 0 < i:
                for j in range(i):
                    pre_num = int(order[j])
                    if first == num and second == pre_num:
                        valid = False

            # after
            if i < len(order) - 1:
                for j in range(i + 1, len(order)):
                    post_num = int(order[j])
                    if second == num and first == post_num:
                        valid = False
    if valid:
        ctr += int(order[len(order) // 2])

print(ctr)
