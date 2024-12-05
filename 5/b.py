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


def is_valid(order):
    for i, num in enumerate(order):
        num = int(num)
        for rule in r:
            first, second = [int(ru) for ru in rule]

            # before
            if 0 < i:
                for j in range(i):
                    pre_num = int(order[j])
                    if first == num and second == pre_num:
                        return False

            # after
            if i < len(order) - 1:
                for j in range(i + 1, len(order)):
                    post_num = int(order[j])
                    if second == num and first == post_num:
                        return False
    return True


def order_nums(order):
    while not is_valid(order):
        for i in range(len(order)):
            for rule in r:
                first, second = [int(ru) for ru in rule]

                # before
                if 0 < i:
                    for j in range(i):
                        if first == int(order[i]) and second == int(order[j]):
                            order[j] = first
                            order[i] = second

                # after
                if i < len(order) - 1:
                    for j in range(i + 1, len(order)):
                        if second == int(order[i]) and first == int(order[j]):
                            order[i] = first
                            order[j] = second
    return order


for order in o:
    if not is_valid(order):
        order = order_nums(order)
        print(order)
        ctr += int(order[len(order) // 2])


print(ctr)
