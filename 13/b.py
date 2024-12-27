import numpy as np

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
            info.extend([int(x) + int(10000000000000) for x in line.split(": ")[1].replace("X=", "").replace("Y=", "").replace("\n", "").split(", ")])
            automates.append(info)
        if info_type == 3:
            info = []
        info_type = (info_type + 1) % 4

price = 0
for i, automate in enumerate(automates):
    possible_prices = []
    x1, y1, x2, y2, tx, ty = automate
    a, b = np.linalg.solve([[x1, x2], [y1, y2]], [tx, ty])
    a, b = float(a), float(b)
    if abs(a - round(a)) < 0.001 and abs(b - round(b)) < 0.001:
        price += round(a)*3+round(b)
print(price)
