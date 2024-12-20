automates = []
info_type = 0
info = []
with open("input", "r") as inp:
    for line in inp:
        if info_type == 0:
            info.extend([int(x) for x in line.split(": ")[1].replace("X+", "").replace("Y+", "").replace("\n", "").split(", ")])
        if info_type == 1:
            info.extend([int(x) for x in line.split(": ")[1].replace("X+", "").replace("Y+", "").replace("\n", "").split(", ")])
        if info_type == 2:
            info.extend([int(x) for x in line.split(": ")[1].replace("X=", "").replace("Y=", "").replace("\n", "").split(", ")])
            automates.append(info)
        if info_type == 3:
            info = []
        info_type = (info_type + 1) % 4

price = 0
for automate in automates:
    possible_prices = []
    x1, y1, x2, y2, tx, ty = automate
    for i in range(1, 100):
        for j in range(1, 100):
            if i * x1 + j * x2 == tx and i * y1 + j * y2 == ty:
                possible_prices.append(i * 3 + j)
    if len(possible_prices) > 0:
        price += min(possible_prices)

print(price)

